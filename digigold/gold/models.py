from django.db import models
from users.models import GoldUser


class DigitalGold(models.Model):
	BOUGHT = 'BG'
	SOLD = 'SD'
	TRADE_STATUS = [
			(BOUGHT, 'Bought'),
			(SOLD, 'Sold')
			]
	tradeStatus = models.CharField(
			max_length=2,
			choices=TRADE_STATUS
			)
	weight = models.DecimalField(max_digits=50, decimal_places=20)
	dateBought = models.DateTimeField(auto_now_add=True)
	rate = models.DecimalField(max_digits=50, decimal_places=20)
	goldUser = models.ForeignKey(GoldUser,on_delete=models.CASCADE)
	transactionId = models.CharField(max_length=255)
	completed = models.BooleanField(default=False)

	def __str__(self):
		return self.goldUser.username

	def get_user_account_number(self):
		return self.goldUser.accountNumber

	def get_status(self):
		return self.tradeStatus

	class Meta:
		ordering = ['-dateBought']
