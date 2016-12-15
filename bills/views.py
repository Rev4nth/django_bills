from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone

import pdb

from .models import Account, Bill
# Create your views here.
def accounts(request):
    accounts =  Account.objects.all()
    template_values = {
        'accounts' : accounts
    }
    return render(request, 'accounts.html', template_values)


def createAccount(request):
    new_account = request.POST.get("new_account")
    create_account = Account(account_name = new_account, created_date= timezone.now())
    create_account.save()
    return HttpResponseRedirect(reverse('bills:accounts'))

def accountBills(request, account_id):
    if request.method == 'POST':
        account = Account.objects.get(pk=account_id)
        name = request.POST.get('bill_name')
        amount = request.POST.get('bill_amount')
        date =  request.POST.get('bill_date')
        account.bill_set.create(bill_name=name, bill_amount=amount, bill_date=date)
        return HttpResponseRedirect(reverse('bills:account_bills', kwargs={'account_id':account_id}))

    else:
        account = Account.objects.get(pk=account_id)
        account_bills = account.bill_set.all()
        template_values = {
            'account': account,
            'account_bills':account_bills
        }
        return render(request, 'account_bills.html', template_values)
