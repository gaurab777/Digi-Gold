from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='gold_index'),
    path('trade/', views.trade, name='gold_trade'),
    path('stripe/webhook/', views.stripeWebhook, name='stripe_webhook'),
    path('success/', views.paymentSuccess, name='pay_sucess'),
    path('cancel/', views.paymentCancel, name='pay_cancel'),
    path('digigold/buy/', views.buyGold, name='gold_buy'),
    path('digigold/sell/',
		views.sellGold, name='gold_sell'),
]
