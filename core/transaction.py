from django.shortcuts import render, redirect
from django.contrib import messages
from account.models import Account
from django.db.models import Q
from .models import Transaction
from django.contrib.auth.decorators import login_required



def transaction_list(request):
    transaction_sender = Transaction.objects.filter(sender = request.user).order_by("-id")
    transaction_reciver = Transaction.objects.filter(reciver = request.user).order_by("-id")

    context = {
        "transaction_sender":transaction_sender,
        "transaction_reciver":transaction_reciver,
    }


    return render(request, 'transaction/transaction_list.html', context)




@login_required
def transaction_detail(request, transaction_id):
    transaction = Transaction.objects.get(transaction_id = transaction_id)

    context = {
        "transaction":transaction,
    }


    return render(request, 'transaction/transaction_detail.html', context)