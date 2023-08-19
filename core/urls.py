from django.urls import path
from .views import index
from .transfare import search_using_account


app_name = 'core'



urlpatterns = [
    path("", index, name='index'),
    path('search-account/', search_using_account, name='search-account')
]
