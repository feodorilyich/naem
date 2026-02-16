from django.db import models
from products.models import Product
from users.models import User


class CartQuerySet(models.QuerySet):
    def total_price(self):
        return sum(cart.product_price() for cart in self)
    
    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0

class Cart(models.Model):
    user = models.ForeignKey(User, verbose_name=("Пользователь"),null=True, blank=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name=("Товар"), on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name="Количество")
    created_timestamp = models.DateTimeField(verbose_name="Момент создания", auto_now_add=True)
    session_key = models.CharField(max_length=32, null=True, blank=True, verbose_name="ключ сессии")

    objects = CartQuerySet.as_manager()

    class Meta:
        db_table = "carts"
        verbose_name = "корзина"
        verbose_name_plural = "корзины"

    def __str__(self):
        return f"корзина -> {self.user.username} | {self.product} | {self.quantity}"
    
    def product_price(self):
        return round(self.product.price_disc()*self.quantity, 2)
    
