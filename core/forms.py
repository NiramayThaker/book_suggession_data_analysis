from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RatingForm(forms.Form):
    Rating = forms.IntegerField()

class BookCategory(forms.Form):
    Category = forms.CharField(max_length=255)

class CustomDataInput(forms.Form):
    Book_Title = forms.CharField(max_length=255)


class RegisterForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ['username',  'email', 'password1', 'password2']
