# dappx/forms.py
from django import forms
from pages.models import UserProfileInfo,Movies_poster
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
	"""password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')"""
		
	password=forms.CharField(widget=forms.PasswordInput())
	confirm_password=forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model=User
		fields=('username','email','password')

	def clean(self):
		cleaned_data = super(UserForm, self).clean()
		password = cleaned_data.get("password")
		confirm_password = cleaned_data.get("confirm_password")

		if password != confirm_password:
			raise forms.ValidationError(
                "password and confirm_password does not match"
            )

class MoviesForm(forms.ModelForm):
    class Meta():
        model = Movies_poster
        fields = ('name', 'movie_Img','video')
		
