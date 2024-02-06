from django.contrib import admin
from accounts.models import Account

class AccountAdmin(admin.ModelAdmin):
    list_display = ['full_name','phone','email','user_type']


# Register your models here.
admin.site.register(Account,AccountAdmin)


