# dappx/forms.py
from django import forms
from pages.models import UserProfileInfo,Movies_poster
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')

class MoviesForm(forms.ModelForm):
    class Meta():
        model = Movies_poster
        fields = ('name', 'movie_Img')