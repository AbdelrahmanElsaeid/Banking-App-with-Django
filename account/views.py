from django.shortcuts import render, redirect
from .forms import KYCForm
from .models import KYC, Account
from django.contrib import messages

# Create your views here.


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
        }

    return render(request, "account/kyc-form.html", context)           