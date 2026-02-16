from django.contrib import admin
from carts.models import Cart

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'created_timestamp')
    readonly_fields = ('created_timestamp',)