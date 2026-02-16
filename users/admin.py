from django.contrib import admin
from orders.admin import OrderTabularAdmin
from carts.models import Cart
from users import models


class CartTabAdmin(admin.TabularInline):
    model = Cart
    fields = ("product","quantity","created_timestamp")
    readonly_fields = ("created_timestamp",)
    extra = 1


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    

    inlines = (CartTabAdmin,OrderTabularAdmin)