from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models

# Create your models here.
class BankUser (models.Model):
	user = models.OneToOneField(User)
	first_digit = models.CharField(max_length=7,null=True, blank=True)
	second_digit = models.CharField(max_length=7,null=True, blank=True)
	third_digit = models.CharField(max_length=7,null=True, blank=True)
	fourth_digit = models.CharField(max_length=7,null=True, blank=True)
	fifth_digit = models.CharField(max_length=7,null=True, blank=True)
	sixth_digit = models.CharField(max_length=7,null=True, blank=True)
	account_number = models.CharField(max_length=16,null=True,blank=True,unique=True)
	ifsc_code = models.CharField(max_length=11,null=True,blank=True)
	amount = models.IntegerField(null=True,blank=True)
	address = models.TextField(max_length=100,null=True,blank=True)
	phone_number = models.CharField(max_length=10,null=True,blank=True)
	dob = models.DateField(null=True,blank=True)

	def __str__(self):
		return self.user.first_name + " " + self.user.last_name


