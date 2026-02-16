from django.urls import path

from carts import views

app_name = 'carts'

urlpatterns = [
    path('add/<slug:product_slug>', views.cart_add, name='add'),
    path('remove/<int:id>', views.cart_remove, name='remove'),
    path('increment/<int:id>', views.cart_increment, name='increment'),
    path('decriment/<int:id>', views.cart_decrement, name='decrement'),]
    