from django import forms
from django.contrib.auth.models import User



class SignupForm(forms.ModelForm):
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
