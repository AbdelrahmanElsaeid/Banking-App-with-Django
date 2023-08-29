from django.urls import path
from .views import index
from .transfare import search_using_account, AmountTranfare, AmountTranfareProcess,TransactionConfirmation,TransfarProcess, TransfarCompleted
from .transaction import transaction_list, transaction_detail
from .payment_request import SearchUserRequest, AmountRequest, AmountRequestProcess, RequestConfirmation, RequestCompleted, RequestFinialProcess, settlement_confirmation, settlement_processing, SettlementCompleted, delete_payment_request
from .credit_card import credit_card_detail, fund_credit_card, withdraw_credit_card, delete_card


app_name = 'core'



urlpatterns = [
    path("", index, name='index'),
    path('search-account/', search_using_account, name='search-account'),
    path('amount-transfare/<account_number>/',AmountTranfare , name='amount-transfare'),
    path('amount-transfare-process/<account_number>/',AmountTranfareProcess , name='amount-transfare-Process'),
    path('transfare-confirm/<account_number>/<transaction_id>/',TransactionConfirmation , name='transfare-confirmation'),
    path('transfare-process/<account_number>/<transaction_id>/',TransfarProcess , name='transaction-process'),
    path('transfare-completed/<account_number>/<transaction_id>/',TransfarCompleted , name='transfar-completed'),



    #transaction



    path('transaction/',transaction_list, name='transaction-list' ),
    path('transaction/<transaction_id>',transaction_detail, name='transaction-detail' ),

    #payment_request

    path('request-search-user/',SearchUserRequest, name='request-search-user' ),
    path('amount-request/<account_number>',AmountRequest, name='amount-request' ),
    path('amount-request-process/<account_number>/',AmountRequestProcess , name='amount-request-Process'),
    path('request-confirm/<account_number>/<transaction_id>/',RequestConfirmation , name='request-confirmation'),
    path('request-process/<account_number>/<transaction_id>/',RequestFinialProcess , name='request-finial-process'),
    path('request-completed/<account_number>/<transaction_id>/',RequestCompleted , name='request-completed'),
    path('settlement-confirmation/<account_number>/<transaction_id>/', settlement_confirmation, name='settlement-confirmation'),
    path('settlement-processing/<account_number>/<transaction_id>/',settlement_processing, name= 'settlement_processing'),
    path('settlement-completed/<account_number>/<transaction_id>/',SettlementCompleted , name='settlement-completed'),
    path('delete-request/<account_number>/<transaction_id>/',delete_payment_request , name='delete-request'),

    # credit_card

    path('card/<card_id>/', credit_card_detail, name="card_detail" ),
    path('fund-credit-card/<card_id>/',fund_credit_card, name= "fund-credit-card" ),
    path('withdraw-credit-card/<card_id>/',withdraw_credit_card, name= "withdraw-credit-card" ),
    path('delete-credit-card/<card_id>/',delete_card, name= "delete-card" ),




]
