from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True,verbose_name="название")
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True, verbose_name="URL")

    class Meta:
        db_table = "categories"
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ("id",)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100, unique=True,verbose_name="название")
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True,verbose_name="URL")
    price = models.DecimalField(max_digits=8, decimal_places=2,default=0.00,verbose_name="цена")
    discount = models.PositiveIntegerField(default=0, verbose_name="скидка")
    description = models.TextField(verbose_name="описание")
    quantity = models.PositiveIntegerField(default=0,verbose_name="количество(осталось)")
    category = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name="категория")
    image =  models.ImageField(upload_to="product_images", blank=True,null=True,verbose_name="картинка")
    
    def price_disc(self):
        return round(self.price - self.price*self.discount/100,2)

    def display_id(self):
        return f'{self.id:07}'

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse("catalog:product", kwargs={"product_slug": self.slug})
    