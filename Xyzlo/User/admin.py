from django.contrib import admin
from User.models import Account
from User.models import Product
# Register your models here.

class AccountA(admin.ModelAdmin):
    list_display = ('name', 'email', 'bdate', 'address', 'pnumber')
    list_filter = ('email', 'name', )


class ProductA(admin.ModelAdmin):
    list_display = ('product_id', 'product_name', 'product_price', 'product_category')
    list_filter = ('pro_email', 'product_price', 'product_category', )


admin.site.register(Account, AccountA)

admin.site.register(Product , ProductA)

admin.site.site_header = "Xyzlo"


