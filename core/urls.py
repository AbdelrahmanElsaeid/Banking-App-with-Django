from django.urls import path
from .views import index
from .transfare import search_using_account, AmountTranfare, AmountTranfareProcess,TransactionConfirmation,TransfarProcess, TransfarCompleted


app_name = 'core'



urlpatterns = [
    path("", index, name='index'),
    path('search-account/', search_using_account, name='search-account'),
    path('amount-transfare/<account_number>/',AmountTranfare , name='amount-transfare'),
    path('amount-transfare-process/<account_number>/',AmountTranfareProcess , name='amount-transfare-Process'),
    path('transfare-confirm/<account_number>/<transaction_id>/',TransactionConfirmation , name='transfare-confirmation'),
    path('transfare-process/<account_number>/<transaction_id>/',TransfarProcess , name='transaction-process'),
    path('transfare-completed/<account_number>/<transaction_id>/',TransfarCompleted , name='transfar-completed'),


]
