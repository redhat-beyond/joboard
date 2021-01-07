from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserAccount


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'password': forms.PasswordInput()
        }


class AccountForm(forms.ModelForm):

    class Meta:
        model = UserAccount
        fields = ['gender', 'birth_date', 'contact_number']
