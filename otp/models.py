from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.contrib import admin

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
	address = models.CharField(max_length=100,null=True,blank=True)
	phone_number = models.CharField(max_length=10,null=True,blank=True)
	BankUser_type = models.IntegerField(null=True,blank=True)
	number_of_logins = models.IntegerField(null=True,blank=True,default=0)

	def name(self):
		return self.user.first_name + " " + self.user.last_name
	name.short_description = 'Name'

class BankUserAdmin (admin.ModelAdmin):
	list_display = ('name','account_number','ifsc_code','BankUser_type','amount','number_of_logins',)

class RegisterLog (models.Model):
	timestamp = models.DateTimeField (blank=True, null=True)
	username = models.CharField(max_length=30,null=True, blank=True)
	time = models.FloatField(null=True,blank=True)
	attempts = models.IntegerField(null=True,blank=True)

	def __str__(self):
		return self.username
	def avgTime(self):
		return (self.time/self.attempts)
	avgTime.short_description = 'Avg Time'

class RegisterLogAdmin (admin.ModelAdmin):
	list_display = ('username','timestamp','time','attempts','avgTime',)

class LoginLog (models.Model):
	timestamp = models.DateTimeField (blank=True, null=True)
	username = models.CharField(max_length=30,null=True, blank=True)
	time = models.FloatField(null=True,blank=True)
	attempts = models.IntegerField(null=True,blank=True)

	def __str__(self):
		return self.username

	def avgTime(self):
		return (self.time/self.attempts)
	avgTime.short_description = 'Avg Time'

class LoginLogAdmin (admin.ModelAdmin):
	list_display = ('username','timestamp','time','attempts','avgTime',)

