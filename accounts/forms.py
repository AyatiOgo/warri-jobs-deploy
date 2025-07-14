from django import forms
from .models import RegularUSer
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class RegularUserCreationForm(UserCreationForm):
    class Meta:
        model = RegularUSer
        fields = ['username','full_name', 'email', 'phone', 'password1', 'password2']
        # full_name=forms.CharField(max_length=100, label="Name")
        # email=forms.EmailField(max_length=100, label="Name")
        # phone=forms.CharField(max_length=20, label="Name")



class RegularUSerLoginForm(AuthenticationForm):
    username = forms.EmailField(label='Email')
    class Meta:
        model = RegularUSer
        fields = ['email', 'password']