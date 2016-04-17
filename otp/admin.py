from django.contrib import admin
from .models import BankUser, RegisterLog, LoginLog, RegisterLogAdmin, LoginLogAdmin, BankUserAdmin

# Register your models here.

admin.site.register(BankUser,BankUserAdmin)
admin.site.register(RegisterLog, RegisterLogAdmin)
admin.site.register(LoginLog, LoginLogAdmin)
