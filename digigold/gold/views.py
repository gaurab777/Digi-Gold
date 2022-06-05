import stripe
from django import forms
from datetime import date
from decimal import Decimal
from django.views import View
from .models import DigitalGold
from django.conf import settings
from users.models import GoldUser
from django.forms import ModelForm
from django.contrib import messages
from django.http import HttpResponse
from .gold import goldPrice,changeRate
from django.views.generic import CreateView
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

today = date.today()
goldType,goldRate = goldPrice()
stripe.api_key = settings.STRIPE_SECRET_KEY
goldProduct = stripe.Product.create(name="DigitalGold")
endpoint_secret = "whsec_e5a161efe430670fb90468938a780ccea2eb68d31b7d31a4bef5c4bcdb679353"
buyform = None
requestuser = None

def index(request):
	global goldType,goldRate,today
	if(date.today() != today):
		today = date.today()
		goldType,goldRate = goldPrice()
	context = {
			"title": "Home",
			"goldRate": goldRate,
			"goldType": goldType
			}
	return render(request, 'gold/gold.html',context)

def trade(request):
	global goldType,goldRate,today
	if(date.today() != today):
		today = date.today()
		goldType,goldRate = goldPrice()
	context = {
			"title": "Trade",
			"goldRate": goldRate,
			"goldType": goldType
			}
	return render(request, 'gold/trade.html',context)

class goldForm(ModelForm):
	class Meta:
		model = DigitalGold
		fields = ['weight', 'rate']

@login_required
def buyGold(request):
	if request.method == 'POST':
		form = goldForm(request.POST)
		form.instance.goldUser = request.user
		form.instance.tradeStatus = 'BG'
		if form.is_valid():
			price = stripe.Price.create(
					product=goldProduct.id,
					unit_amount=int(form.instance.rate*100),
					currency='npr',
					)
			YOUR_DOMAIN = "http://127.0.0.1:8000"
			checkout_session = stripe.checkout.Session.create(
					line_items=[
						{
							'price': price.id,
							'quantity': 1,
							},
						],
					metadata = {
						},
					mode='payment',
					success_url=YOUR_DOMAIN + '/success/',
					cancel_url=YOUR_DOMAIN + '/cancel/',
					)
			global buyform,requestuser
			buyform = goldForm(request.POST)
			buyform.instance.weight = request.POST["weight"]
			requestuser = request.user
			return redirect(checkout_session.url, code=303)

	global goldType,goldRate,today
	if(date.today() != today):
		today = date.today()
		goldType,goldRate = goldPrice()
	if(goldRate == -1):
		messages.error(request, 'Server Error, Try again later!')
		return redirect('gold_index')

	form = goldForm()
	context = {
			"goldrate" : goldRate,
			"goldType" : goldType,
			"form" : form
			}
	return render(request, 'gold/digitalgold_form.html',context)

@csrf_exempt
def stripeWebhook(request):
	payload = request.body
	sig_header = request.META['HTTP_STRIPE_SIGNATURE']
	event = None

	try:
		event = stripe.Webhook.construct_event(
				payload, sig_header, endpoint_secret
				)
	except ValueError as e:
		return HttpResponse(status=400)
	except stripe.error.SignatureVerificationError as e:
		return HttpResponse(status=400)

	if event['type'] == 'checkout.session.completed':
		session = event['data']['object']
		print(session)
		buyform.instance.goldUser = requestuser
		buyform.instance.tradeStatus = 'BG'
		buyform.instance.transactionId = session["id"]
		buyform.instance.completed = True
		added = Decimal(buyform.instance.weight)
		currentWeight = requestuser.get_current_goldWeight()
		GoldUser.objects.filter(username=requestuser.username).update(goldWeight=currentWeight + added)
		buyform.save()

	return HttpResponse(status=200)

@login_required
def sellGold(request):
	if request.method == 'POST':
		form = goldForm(request.POST)
		form.instance.goldUser = request.user
		form.instance.tradeStatus = 'SD'
		sub = Decimal(request.POST["weight"])
		currentWeight = request.user.get_current_goldWeight()
		if(currentWeight < sub):
			messages.error(request,"You don't have enought digital gold to sell")
			return redirect("gold_sell")
		GoldUser.objects.filter(username=request.user.username).update(goldWeight=currentWeight - sub)
		messages.success(request,"Your transaction will be verified and amount will be deposited to your account within 3 business days.")
		form.save()
		return redirect("gold_index")
	global goldType,goldRate,today
	if(date.today() != today):
		today = date.today()
		goldType,goldRate = goldPrice()
	if(goldRate == -1):
		messages.error(request, 'Server Error, Try again later!')
		return redirect('gold_index')

	form = goldForm()
	context = {
			"goldrate" : goldRate,
			"goldType" : goldType,
			"form" : form
			}
	return render(request, 'gold/digigold_sell.html',context)

@login_required
def paymentSuccess(request):
	context = {
			"title": "PaymentSuccessfull"
			}
	return render(request, 'gold/paysuccess.html',context);

@login_required
def paymentCancel(request):
	context = {
			"title": "PaymentCancelled"
			}
	return render(request, 'gold/paycancel.html',context);
