from django.shortcuts import render, redirect
from .forms import KYCForm
from .models import KYC, Account
from django.contrib import messages

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
    form = KYCForm(request.POST, request.FILES, instance=kyc)
    if form.is_valid():
        new_form = form.save(commit=False)
        new_form.user = user
        new_form.account = account
        new_form.save()
        messages.success(request, "KYC Form submitted successfully")
        return redirect("core:index")

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
            return redirect("account:kyc-form")

        account = Account.objects.get(user=user)
    else:
        messages.warning(request, "You Need To Login")
        return redirect("userauths:sign-in")
    context = {
        'account':account,
        'kyc':kyc,
    }
    return render(request, 'account/dashboard.html', context)
