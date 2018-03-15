from django import forms
from django.contrib.auth.models import User
from HotPotWebsite.models import Dish, MenuCategory, UserProfile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('zipcode', 'headpicture')