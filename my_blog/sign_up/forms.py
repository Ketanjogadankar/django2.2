from django.forms import ModelForm
# from .models import Order
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from sign_up.models import Post

# class OrderForm(ModelForm):
#     class Meta:
#         model = Order
#         fields = '__all__'

class CreateUserForms(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']

class HomeForm(forms.ModelForm):
    post = forms.CharField(label='Post')
    class Meta:
        model = Post
        fields = ['post']

