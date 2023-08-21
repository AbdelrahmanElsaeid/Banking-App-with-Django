from django.urls import path
from .views import kyc_registration, account,Dashboard



app_name = 'account'

urlpatterns = [
    path("",account , name='account'),
    path("dashboard",Dashboard , name='dashboard'),

    path("kyc-reg/",kyc_registration, name='kyc-reg'),
  

]
