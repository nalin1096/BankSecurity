from __future__ import unicode_literals
from django.contrib.auth.models import User

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

	def __str__(self):
		return self.sender + " to " + self.receiver


