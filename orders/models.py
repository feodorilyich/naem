from django.db import models

from users.models import User
from products.models import Product


class Order(models.Model):
    user = models.ForeignKey(to=User,on_delete=models.SET_NULL,null=True,blank=True,verbose_name="пользователь")
    created_timestap = models.DateTimeField(auto_now_add=True,verbose_name="время создания")
    phone_number = models.CharField(max_length=13,verbose_name="телефон")
    requires_delivery = models.BooleanField(default=False,verbose_name="требуется доставка")
    delivery_address = models.TextField(null=True,blank=True,verbose_name="адрес доставки")
    payment_on_get = models.BooleanField(default=False,verbose_name="оплата при получении")
    is_paid = models.BooleanField(default=False,verbose_name="оплачен")
    status = models.CharField(max_length=36,default="в обработке...",verbose_name="статус")
    
    class Meta:
        db_table = "orders"
        verbose_name = "заказ"
        verbose_name_plural = "заказы"

    def __str__(self):
        return f"заказ№{self.pk} | {self.user.first_name}  {self.user.last_name}"

class OrderItemQuerySet(models.QuerySet):
    def total_price(self):
        return sum(cart.products_price() for cart in self)
    
    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0
    
class OrderItem(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE, verbose_name="заказ")
    product = models.ForeignKey(to=Product, on_delete=models.SET_NULL, null=True, verbose_name="продукт")
    name = models.CharField(max_length=255, verbose_name="имя")
    price = models.DecimalField(max_digits=6, decimal_places=2,verbose_name="цена")
    quantity = models.PositiveIntegerField(default=0, verbose_name="количество")
    created_timestamp = models.DateTimeField(auto_now_add=True,verbose_name="время создания")

    objects = OrderItemQuerySet.as_manager()

    class Meta:
        db_table = "order_items"
        verbose_name = "товар в заказе"
        verbose_name_plural = "товары в заказе"

    def products_price(self):
        return round(self.price * self.quantity, 2)

    def __str__(self):
        return f"{self.name} | кол-во {self.quantity} | заказ №{self.order.pk}"