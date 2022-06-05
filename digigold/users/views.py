from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import GoldRegistrationForm,GoldUserChangeForm

def userRegister(request):
    if request.method == 'POST':
        form = GoldRegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created! Login to continue.')
            return redirect('users_login')
    else:
        form = GoldRegistrationForm()
    context = {
        "form": form,
        "title": "Register"
            }
    return render(request, 'users/register.html',context)

@login_required
def userProfile(request):
    if request.method != 'POST':
        form = GoldUserChangeForm(instance=request.user)
    else:
        form = GoldUserChangeForm(request.POST,request.FILES,instance=request.user)
        if form.is_valid():
            form.save()
    context = {
        "user_change_form": form,
        "title": "MyProfile"
    }
    return render(request, 'users/prof.html',context);

def aboutUs(request):
	return render(request, 'users/aboutus.html')

def contactUs(request):
	return render(request, 'users/contactus.html')

def frontpage(request):
	return render(request, 'users/frontpages.html')
