from django.shortcuts import render, redirect
from django.contrib import messages
from account.models import Account
from django.db.models import Q
from .models import Transaction, Notification
from decimal import Decimal


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




def AmountTranfareProcess(request, account_number):
    account = Account.objects.get(account_number=account_number)
    sender = request.user
    reciver = account.user

    sender_account = request.user.account
    reciver_account = account


    if request.method=="POST":
        amount = request.POST.get("amount-send")
        description = request.POST.get("description")

        if sender_account.account_balance >= Decimal(amount):
            new_transaction = Transaction.objects.create(
                user = request.user,
                amount = amount,
                sender = sender,
                reciver = reciver,
                sender_account = sender_account,
                reciver_account = reciver_account,
                description = description,
                transaction_type = "transfer",
                status = "processing",
            )

            new_transaction.save()
            transaction_id = new_transaction.transaction_id

            return redirect("core:transfare-confirmation", account.account_number, transaction_id)
        
        else:
            messages.warning(request, 'Insufficient fund')
            return redirect("core:amount-transfare", account.account_number)

    else:
        messages.warning(request, 'Error Occured, Try again later .')
        return redirect("account:account")

         


def TransactionConfirmation(request, account_number, transaction_id):
    try:
        account = Account.objects.get(account_number=account_number)
        transaction = Transaction.objects.get(transaction_id=transaction_id)
    except:
        messages.warning(request, 'Transaction Does not exists')
        return redirect('account:account') 


    context = {'account':account,
               'transaction':transaction
               }       
    
    return render(request, 'transfare/transaction-confirmation.html', context)




def TransfarProcess(request,account_number, transaction_id):
    account = Account.objects.get(account_number=account_number)
    transaction = Transaction.objects.get(transaction_id=transaction_id)

    sender = request.user
    reciver = account.user

    sender_account = request.user.account
    reciver_account = account
    
    completed = False
    if request.method=="POST":
        pin_num = request.POST.get('pin-number')
        print(pin_num)


        if pin_num == sender_account.pin_number:

            transaction.status = "completed"
            transaction.save()

            sender_account.account_balance -= transaction.amount
            sender_account.save()
            reciver_account.account_balance += transaction.amount
            reciver_account.save()


            Notification.objects.create(
                amount=transaction.amount,
                user=account.user,
                notification_type="Credit Alert"
            )
            
            Notification.objects.create(
                user=sender,
                notification_type="Debit Alert",
                amount=transaction.amount
            )

            messages.success(request, "Transfar Successfull.")
            return redirect("core:transfar-completed" ,account.account_number ,transaction.transaction_id)
        else:
            messages.warning(request, "Incorrect Pin Number.")
            return redirect("core:transfare-confirmation",account.account_number ,transaction.transaction_id)
        
    else:
        messages.warning(request, "An Error occured, Try again later.")
        return redirect("account:account")    



def TransfarCompleted(request ,account_number, transaction_id):
    try:
        account = Account.objects.get(account_number=account_number)
        transaction = Transaction.objects.get(transaction_id=transaction_id)

    except:
        messages.warning(request, 'Transfare does not exists')
        return redirect("account:account")
    
    context = {'account':account,
               'transaction':transaction
               } 
    return render(request, 'transfare/transfar-completed.html', context)    