from django.shortcuts import render
from users.forms import UserLoginForm, UserRegistrationForm, ProfileForm
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Prefetch
from django.contrib.auth.decorators import login_required
from orders.models import Order,OrderItem


def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)

        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request,"Вы вошли в аккаунт!")
                return HttpResponseRedirect(reverse("main:index"))
    else:
        form = UserLoginForm()

    context = {"name":"login",
               "form":form}
    return render(request,'login.html',context)

@login_required(login_url="/user/login/")
def logout(request):
    messages.warning(request,"Вы вышли из аккаунта.")
    auth.logout(request)
    return HttpResponseRedirect(reverse("main:index"))

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"вы создали аккаунт!")
            user = form.instance
            auth.login(request,user)
            return HttpResponseRedirect(reverse("main:index"))
    else:
        form = UserRegistrationForm()
    context = {"name":"register","form":form}
    return render(request,'registration.html',context)

@login_required(login_url="/user/login/")
def profile(request):
    if request.method == "POST":
        form = ProfileForm(data=request.POST,
                           files=request.FILES,
                           instance=request.user)
        
        if form.is_valid():
            form.save()
            messages.success(request,"Профиль обновлён.")
            return HttpResponseRedirect(reverse("user:profile"))
    else:
        form = ProfileForm(instance=request.user)

        orders = Order.objects.filter(user=request.user).prefetch_related(Prefetch("orderitem_set",queryset=OrderItem.objects.select_related("product"))).order_by('-id')

    context = {"name":"profile","form":form,"orders":orders}
    return render(request,'profile.html',context)

def user_cart(request):
    return render(request,'user_cart.html')