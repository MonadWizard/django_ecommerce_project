from django.contrib import admin

from order.models import ShopCart
# Register your models here.

class ShopCartAdmin(admin.ModelAdmin):
    list_display = ['product','user', 'quantity', 'price', 'amount']
    list_filter = ['user']








admin.site.register(ShopCart,ShopCartAdmin)








