from django.shortcuts import HttpResponse,redirect,get_object_or_404
from products.models import Product
from carts.models import Cart


def cart_add(request,product_slug):
    product = Product.objects.get(slug=product_slug)

    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product)
        if carts.exists():
            cart = carts.first()
            cart.quantity += 1
            cart.save()
        else:
            Cart.objects.create(user=request.user, product=product, quantity=1)
    return redirect(request.META.get("HTTP_REFERER", "/"))

def cart_remove(request,id):
    id = Cart.objects.get(id=id)
    id.delete()
    return redirect(request.META.get("HTTP_REFERER", "/"))

def cart_increment(request,id):
    cart = get_object_or_404(Cart,id=id)
    cart.quantity += 1
    cart.save()
    return redirect(request.META.get("HTTP_REFERER", "/"))

def cart_decrement(request,id):
    cart = get_object_or_404(Cart,id=id)
    if cart.quantity > 1:
        cart.quantity -= 1
        cart.save()
    else:
        cart.delete()
    return redirect(request.META.get("HTTP_REFERER", "/"))
