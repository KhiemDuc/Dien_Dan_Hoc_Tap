from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Room, User
import re
from django.core.exceptions import ObjectDoesNotExist
from django import forms


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['nickname', 'username', 'email', 'password1', 'password2',]
    


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'name','nickname', 'email', 'bio',]
