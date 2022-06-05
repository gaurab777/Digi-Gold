from PIL import Image
from django.db import models
from django.contrib.auth.models import AbstractUser

class GoldUser(AbstractUser):
	genderM = 'M'
	genderF = 'F'
	genderUK = 'U'
	genderCHOICES = [(genderM, 'Male'), (genderF, 'Female'),(genderUK, 'Dont Know')]
	gender = models.CharField(max_length=1,choices=genderCHOICES)
	goldWeight = models.DecimalField(max_digits=40,decimal_places=20,default=0,blank=True)
	accountNumber = models.CharField(max_length=255)

	def __str__(self):
		return self.username + f"-{self.accountNumber}"

	def get_gender(self):
		return self.gender

	def get_current_goldWeight(self):
		return self.goldWeight
