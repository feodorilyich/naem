from django.urls import path


from main import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('about_us/',views.about, name='about'),]

