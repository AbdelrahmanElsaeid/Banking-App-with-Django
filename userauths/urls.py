from django.urls import path
from .views import RegisterView, LoginView, LogoutView



app_name = 'userauths'






urlpatterns = [
    path("sign-up/",RegisterView, name='sign-up'),
    path("sign-in/",LoginView, name='sign-in'),
    path("sign-out/",LogoutView, name='sign-out'),

]
