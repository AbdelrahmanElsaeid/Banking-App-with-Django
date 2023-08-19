from django.shortcuts import render, redirect
from django.contrib import messages
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




def AmountTranfare(request, account_number):
    try:
        account = Account.objects.get(account_number=account_number)

    except:
        messages.warning(request, "Account does not exist")



    context = {
        "account":account
    }    


    return render(request, 'transfare/amount-transfare.html', context)