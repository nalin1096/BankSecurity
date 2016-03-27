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

	def __str__(self):
		return self.user.username


