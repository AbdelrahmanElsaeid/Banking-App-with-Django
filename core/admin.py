from django.contrib import admin
from .models import Transaction
# Register your models here.

class TransactionAdmin(admin.ModelAdmin):
    list_editable = ['amount', 'status', 'transaction_type', 'reciver', 'sender']
    list_display = ['user', 'amount', 'status', 'transaction_type','reciver', 'sender']
    

admin.site.register(Transaction, TransactionAdmin)