from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from .models import Account, Bill

def login(request):
    # import pdb; pdb.set_trace()
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('bills:accounts'))
    else:
        return render(request,'login.html')

@login_required
def accounts(request):
    accounts =  Account.objects.all()
    template_values = {
        'accounts' : accounts
    }
    return render(request, 'accounts.html', template_values)

@login_required
def createAccount(request):
    if request.method == 'POST':
        new_account = request.POST.get("new_account")
        create_account = Account(account_name = new_account, created_date= timezone.now())
        create_account.save()
        return HttpResponseRedirect(reverse('bills:accounts'))
    else:
        return HttpResponseRedirect(reverse('bills:account_bills'))

@login_required
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
