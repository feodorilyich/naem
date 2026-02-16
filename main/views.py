from django.shortcuts import render
from products import models

def index(request):
    category = models.Category.objects.all()
    context = {
        "name":"GAME ZONE",
        "categories":category,
    }
    return render(request,'main/index.html',context)

def about(request):
    context = {
        "title": "О нас",
        "description": "много текста о нас",
    }
    return render(request,'main/about.html',context)

