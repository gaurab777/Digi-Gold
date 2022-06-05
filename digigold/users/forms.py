from django import forms
from django.db import models
from .models import GoldUser
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class GoldUserCreationForm(UserCreationForm):
	genderM = 'M'
	genderF = 'F'
	genderUK = 'U'
	genderCHOICES = [(genderM, 'Male'), (genderF, 'Female'),(genderUK, 'Dont Know')]
	gender = models.CharField(max_length=1,choices=genderCHOICES)
	class Meta:
		model = GoldUser
		fields = ['username','email','password1','password2','gender',]

class GoldUserChangeForm(UserChangeForm):
	genderM = 'M'
	genderF = 'F'
	genderUK = 'U'
	genderCHOICES = [(genderM, 'Male'), (genderF, 'Female'),(genderUK, 'Dont Know')]
	gender = models.CharField(max_length=1,choices=genderCHOICES)
	password = None
	class Meta:
		model = GoldUser
		fields = ['first_name','last_name','email','gender',]

class GoldRegistrationForm(UserCreationForm):
	genderM = 'M'
	genderF = 'F'
	genderUK = 'U'
	genderCHOICES = [(genderM, 'Male'), (genderF, 'Female'),(genderUK, 'Dont Know')]
	email = forms.EmailField()
	gender = models.CharField(max_length=1,choices=genderCHOICES)

	def clean_first_name(self):
		if not self.cleaned_data["first_name"].strip():
			raise ValidationError("Specify your First Name.")
		return self.cleaned_data["first_name"]

	def clean_last_name(self):
		if not self.cleaned_data["last_name"].strip():
			raise ValidationError("Specify your Last Name.")
		return self.cleaned_data["last_name"]

	class Meta:
		model = GoldUser
		fields = ['username','first_name','last_name','accountNumber','email','gender','password1','password2',]
