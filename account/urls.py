from django.urls import path
from .views import kyc_registration, account



app_name = 'account'

urlpatterns = [
    path("",account , name='account'),
    path("kyc-reg/",kyc_registration, name='kyc-reg'),
  

]
