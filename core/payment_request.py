from django.shortcuts import render, redirect
from django.contrib import messages
from account.models import Account
from django.db.models import Q
from .models import Transaction
from django.contrib.auth.decorators import login_required
from decimal import Decimal


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




def AmountRequest(request, account_number):
    try:
        account = Account.objects.get(account_number=account_number)

    except:
        messages.warning(request, "Account does not exist")



    context = {
        "account":account
    }    


    return render(request, 'payment_request/amount-request.html', context)



def AmountRequestProcess(request, account_number):
    account = Account.objects.get(account_number=account_number)
    request_sender = request.user
    request_reciver = account.user

    sender_account = request.user.account
    reciver_account = account


    if request.method=="POST":
        amount = request.POST.get("amount-request")
        description = request.POST.get("description")

        new_request = Transaction.objects.create(
            user = request.user,
            amount = amount,
            sender =  request_sender,
            reciver =  request_reciver,
            sender_account = sender_account,
            reciver_account = reciver_account,
            description = description,
            transaction_type = "requested",
            status = "processing",
        )

        new_request.save()
        transaction_id = new_request.transaction_id

        return redirect("core:request-confirmation", account.account_number, transaction_id)
        
    

    else:
        messages.warning(request, 'Error Occured, Try again later .')
        return redirect("account:account")