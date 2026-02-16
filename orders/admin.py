from orders.models import Order,OrderItem
from django.contrib import admin


class OrderItemTabularInline(admin.TabularInline):
    model = OrderItem
    fields = ("product","price")
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "requires_delivery",
        "payment_on_get",
        "is_paid",
        "status",
    )
    search_fields = ("id","user__username")
    list_filter = ("is_paid","payment_on_get","status","requires_delivery")

    inlines = [OrderItemTabularInline]

@admin.register(OrderItem)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "price"
    )
    search_fields = ("id","name")

class OrderTabularAdmin(admin.TabularInline):
    model = Order
    fields = ("user","requires_delivery","payment_on_get","is_paid","status")
    extra = 0


