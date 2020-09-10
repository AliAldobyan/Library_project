from django import forms
from .models import Book
from django.contrib.auth.models import User


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

        widgets = {
        	'year_of_release': forms.DateInput(attrs={'type':'date'}),
        }

class MembershipForm(forms.ModelForm):
    class Meta:
        model = User
        email = forms.EmailField(required=True)
        fields = ['username', 'email' ,'password']

        widgets={
        'password': forms.PasswordInput(),
        }


class SigninForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())
