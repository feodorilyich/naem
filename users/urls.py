from django.urls import path

from users import views

app_name = 'products'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('cart/', views.user_cart, name='user_cart'),]