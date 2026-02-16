from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms

from users.models import User

class UserLoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField()

    Meta = User

    
class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField()
    password2 = forms.CharField()
    class Meta:
        model = User
        fields = ("first_name","last_name","username","email","password1","password2")

    
class ProfileForm(UserChangeForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    image = forms.ImageField()
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ("first_name","last_name","username","email","image")