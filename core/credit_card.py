from decimal import Decimal
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




def fund_credit_card(request, card_id):
    account = request.user.account
    credit_card = CreditCard.objects.get(card_id=card_id)


    if request.method == 'POST':
        amount = request.POST.get("funding_amount")
        
        if Decimal(amount) <= account.account_balance:
            account.account_balance -=Decimal(amount)
            account.save()

            credit_card .amount += Decimal(amount)
            credit_card.save()

            messages.success(request, 'fundin Successfull')
            return redirect("core:card_detail", credit_card.card_id)

        else:
            messages.warning(request, "Insufficient funds, fund your account and try again.")
            return redirect("core:card_detail", credit_card.card_id)
    
