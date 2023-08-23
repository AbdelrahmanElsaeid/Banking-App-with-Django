from django.shortcuts import render, redirect
from django.contrib import messages
from account.models import Account
from django.db.models import Q
from .models import Transaction
from django.contrib.auth.decorators import login_required


@login_required
def SearchUserRequest(request):
    account = Account.objects.all()
    query = request.POST.get('account_number')


    if query:
        account = Account.objects.filter(account_number = query)

    context = {
        "account":account,
        "query":query
    }    


    return render(request, 'payment_request/search-user.html', context)