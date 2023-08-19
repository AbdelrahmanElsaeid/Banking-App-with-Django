from django.shortcuts import render, redirect

from account.models import Account
from django.db.models import Q



def search_using_account(request):
    account = Account.objects.all()

    query = request.POST.get('account_number')
    if query:
        account = Account.objects.filter(
            Q(account_number = query)|
            Q(account_id = query)
                                         ).distinct()


    context = {
        'account':account,
        'query':query
        }
    return render(request, "transfare/search-account.html", context)