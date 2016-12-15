from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


# Create your models here.

@python_2_unicode_compatible
class Account(models.Model):
    account_name = models.CharField(max_length=80)
    created_date = models.DateTimeField('date created')

    def __str__(self):
        return self.account_name

@python_2_unicode_compatible
class Bill(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    bill_name = models.CharField(max_length=80)
    bill_amount = models.IntegerField()
    bill_date =  models.DateField()

    def __str__(self):
        return self.bill_name
