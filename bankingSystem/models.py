from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.contrib import admin

from django.db import models

# Create your models here.
class Transaction (models.Model):

	TRANSFER_TYPES = (
		('Cr','Credit'),
		('Db','Debit'),
	)

	primary_account = models.CharField(max_length=16,null=True, blank=True)
	secondary_account = models.CharField(max_length=16,null=True, blank=True)
	amount = models.IntegerField(null=True,blank=True)
	transfer_type = models.CharField(max_length=2, null=True, blank=True, choices=TRANSFER_TYPES)
	time = models.DateTimeField (blank=True, null=True)
	balance_remaining = models.IntegerField(null=True,blank=True)

	def transaction(self):
		return self.primary_account + " to " + self.secondary_account
	transaction.short_description = 'Transaction'

class TransactionAdmin (admin.ModelAdmin):
	list_display = ('transaction','amount','transfer_type','time','balance_remaining',)

class TransactionLog (models.Model):
	timestamp = models.DateTimeField (blank=True, null=True)
	username = models.CharField(max_length=30,null=True, blank=True)
	primary_account = models.CharField(max_length=16,null=True, blank=True)
	secondary_account = models.CharField(max_length=16,null=True, blank=True)
	time = models.FloatField(null=True,blank=True)
	attempts = models.IntegerField(null=True,blank=True)

	def transaction(self):
		return self.primary_account + " to " + self.secondary_account
	transaction.short_description = 'Transaction'

	def avgTime(self):
		return (self.time/self.attempts)
	avgTime.short_description = 'Avg Time'

class TransactionLogAdmin (admin.ModelAdmin):
	list_display = ('username','transaction','timestamp','time','attempts','avgTime',)


class TransactionConfirmLog (models.Model):
	timestamp = models.DateTimeField (blank=True, null=True)
	username = models.CharField(max_length=30,null=True, blank=True)
	primary_account = models.CharField(max_length=16,null=True, blank=True)
	secondary_account = models.CharField(max_length=16,null=True, blank=True)
	time = models.FloatField(null=True,blank=True)
	attempts = models.IntegerField(null=True,blank=True)

	def transaction(self):
		return self.primary_account + " to " + self.secondary_account
	transaction.short_description = 'Transaction'

	def avgTime(self):
		return (self.time/self.attempts)
	avgTime.short_description = 'Avg Time'

class TransactionConfirmLogAdmin (admin.ModelAdmin):
	list_display = ('username','transaction','timestamp','time','attempts','avgTime',)




