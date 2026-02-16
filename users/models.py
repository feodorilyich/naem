from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    image = models.ImageField(upload_to="users_images",null=True,blank=True,verbose_name="аватар")
    phone_number = models.CharField(max_length=12, verbose_name="номер телефона",null=True,blank=True)

    class Meta:
        db_table = "auth_user"
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"