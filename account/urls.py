from django.urls import path
from .views import kyc_registration



app_name = 'account'

urlpatterns = [
    path("kyc-reg/",kyc_registration, name='kyc-reg'),
  

]
