# from _typeshed import FileDescriptor
# from django.db.models import fields
from account.models import Account
from django.contrib import admin


class AccountAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'email',
        # 'phone_no',
        # 'last_login'
        # 'date_joined',
    )

    readonly_fields = (
        'password',
    )
    
# Register your models here.
admin.site.register(Account, AccountAdmin)
# admin.site.register(User)
# admin.site.register(AccountDetail)
# admin.site.register(MyAccountManager)
    
