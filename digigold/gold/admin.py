from .models import DigitalGold
from django.contrib import admin

class DigitalGoldAdmin(admin.ModelAdmin):
	model = DigitalGold
	readonly_fields = ('goldUser','weight','rate','tradeStatus','transactionId')
	list_display = ('goldUser','weight','rate','tradeStatus','transactionId')
	list_filter = ('goldUser','weight','rate','tradeStatus')
	search_fields = ('transactionId',)
	ordering = ('-dateBought',)

admin.site.register(DigitalGold, DigitalGoldAdmin)

