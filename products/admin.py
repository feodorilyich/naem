from django.contrib import admin
from products import models

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
     prepopulated_fields = {"slug":("name", )}

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
     prepopulated_fields = {"slug":("name", )}
     list_display = ("name","price","category","description","discount",)
     list_editable = ("price","discount")
     search_fields = ("name","description")
     list_filter = ("price","category")