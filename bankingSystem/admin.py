from django.contrib import admin

from .models import Transaction, TransactionAdmin, TransactionLog, TransactionLogAdmin, TransactionConfirmLog, TransactionConfirmLogAdmin

# Register your models here.
admin.site.register(Transaction,TransactionAdmin)
admin.site.register(TransactionLog,TransactionLogAdmin)
admin.site.register(TransactionConfirmLog,TransactionConfirmLogAdmin)