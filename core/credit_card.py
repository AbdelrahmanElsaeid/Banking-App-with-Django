from decimal import Decimal
from django.shortcuts import render, redirect
from .models import  Account
from django.contrib import messages
from core.models import CreditCard, Notification




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

            Notification.objects.create(
                amount=amount,
                user=request.user,
                notification_type="Funded Credit Card"
            )

            messages.success(request, 'funding Successfully')
            return redirect("core:card_detail", credit_card.card_id)

        else:
            messages.warning(request, "Insufficient funds, fund your account and try again.")
            return redirect("core:card_detail", credit_card.card_id)
    


def withdraw_credit_card(request, card_id):
    account = request.user.account
    credit_card = CreditCard.objects.get(card_id=card_id)


    if request.method == 'POST':
        amount = request.POST.get("amount")
        
        if credit_card.amount >= Decimal(amount):
            account.account_balance += Decimal(amount)
            account.save()

            credit_card .amount -= Decimal(amount)
            credit_card.save()

            Notification.objects.create(
                user=request.user,
                amount=amount,
                notification_type="Withdrew Credit Card Funds"
            )

            messages.success(request, 'Withdraw Successfully')
            return redirect("core:card_detail", credit_card.card_id)

        else:
            messages.warning(request, "Insufficient funds, fund your account and try again.")
            return redirect("core:card_detail", credit_card.card_id)
        

def delete_card(request, card_id):
    account = request.user.account
    credit_card = CreditCard.objects.get(card_id=card_id)

    if credit_card.amount  <=0:
        Notification.objects.create(
            user=request.user,
            notification_type="Deleted Credit Card"
        )
        credit_card.delete()
        messages.success(request, "Card Deleted Successfull")
        return redirect("account:dashboard")

    else:
        account.account_balance +=  credit_card.amount 
        account.save() 
        Notification.objects.create(
            user=request.user,
            notification_type="Deleted Credit Card"
        )
        credit_card.delete()

        messages.success(request, "Card Deleted Successfull")
        return redirect("account:dashboard")
