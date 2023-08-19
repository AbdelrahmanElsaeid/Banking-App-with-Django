from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User
# Create your views here.



def RegisterView(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user=form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Hey {username}, your account was created successfully.")
            new_user = authenticate(username=form.cleaned_data['email'],password = form.cleaned_data['password1'])
            login(request, new_user)
            return redirect("core:index")
    if request.user.is_authenticated:
        messages.warning(request, f" You are already logged in.")
        return redirect("core:index")


    else:
         form = UserRegisterForm()
    return render(request,'userauths/sign-up.html',{'form':form})




def LoginView(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")


        try:
            user = User.objects.get(email=email)
            user = authenticate(request, email=email, password = password)

            if user is not None:
                login(request, user)
                messages.success(request, "You are logged.")
                return redirect('core:index')
            else:
                messages.warning(request, "Username or Password does not exist")
                return redirect("userauths:sign-in")
        except:
            messages.warning(request, "User does not exist")

    if request.user.is_authenticated:
        messages.warning(request, "You Are Already Logged In")
        return redirect("account:account")

    return render(request, "userauths/sign-in.html")        



def LogoutView(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('userauths:sign-in')