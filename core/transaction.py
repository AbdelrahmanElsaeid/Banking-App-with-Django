from django.shortcuts import render, redirect
from django.contrib import messages
from account.models import Account
from django.db.models import Q
from .models import Transaction




def transaction_list(request):
    transaction_sender = Transaction.objects.filter(sender = request.user)
    transaction_reciver = Transaction.objects.filter(reciver = request.user)





    context = {
        "transaction_sender":transaction_sender,
        "transaction_reciver":transaction_reciver,
    }


    return render(request, 'transaction/transaction_list.html', context)