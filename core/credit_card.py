from django.shortcuts import render, redirect
from .models import  Account
from django.contrib import messages
from core.models import CreditCard




def credit_card_detail(request, card_id):
    account = Account.objects.get(user=request.user)
    credit_card= CreditCard.objects.get(user = request.user, card_id=card_id)

    context = {
        "account":account,
        "credit_card":credit_card,
    }


    return render(request, 'credit_card/card_detail.html', context)