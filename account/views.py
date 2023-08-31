from django.shortcuts import render, redirect
from .forms import KYCForm
from .models import KYC, Account
from django.contrib import messages
from core.forms import CreditCardForm
from core.models import CreditCard, Transaction
# Create your views here.


def account(request):
    user = request.user

    if request.user.is_authenticated:
        try:
            kyc = KYC.objects.get(user=user)
        except:
            messages.warning(request, "You Need To Submit YOur KYC")
            return redirect("account:kyc-form")

        account = Account.objects.get(user=user)
    else:
        messages.warning(request, "You Need To Login")
        return redirect("userauths:sign-in")
    context = {
        'account':account,
        'kyc':kyc,
    }
    return render(request, 'account/account.html', context)



def kyc_registration(request):
    user = request.user
    account = Account.objects.get(user=user)


    try:
        kyc = KYC.objects.get(user=user)

    except:
        kyc = None
    if request.method == "POST":    
        form = KYCForm(request.POST, request.FILES, instance=kyc)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = user
            new_form.account = account
            new_form.save()
            messages.success(request, "KYC Form submitted successfully")
            return redirect("account:dashboard")

    else:
        form = KYCForm(instance=kyc) 

    context = {
        "account": account,
        "form": form,
        "kyc": kyc,

        }

    return render(request, "account/kyc-form.html", context)           





def Dashboard(request):
    user = request.user

    if request.user.is_authenticated:
        try:
            kyc = KYC.objects.get(user=user)
        except:
            messages.warning(request, "You Need To Submit YOur KYC")
            return redirect("account:kyc-reg")
        
        recent_transfer = Transaction.objects.filter(sender=request.user, transaction_type="transfer", status="completed").order_by("-id")[:1]
        recent_recieved_transfer = Transaction.objects.filter(reciver=request.user, transaction_type="transfer").order_by("-id")[:1]


        sender_transaction = Transaction.objects.filter(sender=request.user, transaction_type="transfer").order_by("-id")
        reciever_transaction = Transaction.objects.filter(reciver=request.user, transaction_type="transfer").order_by("-id")

        request_sender_transaction = Transaction.objects.filter(sender=request.user, transaction_type="request")
        request_reciever_transaction = Transaction.objects.filter(reciver=request.user, transaction_type="request")
        account = Account.objects.get(user=request.user)
        credit_card = CreditCard.objects.filter(user=request.user).order_by("-id")

        if request.method == "POST":
            form = CreditCardForm(request.POST)
            if form.is_valid():
                new_form = form.save(commit=False)
                new_form.user = request.user
                new_form.save()

                card_id = new_form.card_id
                messages.success(request, "Card ADDED Successfully.")
                return redirect("account:dashboard")
        else:
            form = CreditCardForm()
        account = Account.objects.get(user=user)
        credit_card = CreditCard.objects.filter(user=user).order_by("-id")
    else:
        messages.warning(request, "You Need To Login")
        return redirect("userauths:sign-in")
    context = {
        'account':account,
        'kyc':kyc,
        'form':form,
        "credit_card":credit_card,

        "sender_transaction":sender_transaction,
        "reciever_transaction":reciever_transaction,

        'request_sender_transaction':request_sender_transaction,
        'request_reciever_transaction':request_reciever_transaction,
        'recent_transfer':recent_transfer,
        'recent_recieved_transfer':recent_recieved_transfer,
    }
    return render(request, 'account/dashboard.html', context)
