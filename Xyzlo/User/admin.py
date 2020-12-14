from django.contrib import admin
from User.models import Account
# Register your models here.

class AccountA(admin.ModelAdmin):
    list_display = ('name', 'email', 'bdate', 'address', 'pnumber')
    list_filter = ('email', 'name', )

admin.site.register(Account, AccountA)

admin.site.site_header = "Xyzlo"

