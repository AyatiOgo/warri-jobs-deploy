from django import forms
from .models import RegularUSer
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError

class RegularUserCreationForm(UserCreationForm):
    class Meta:
        model = RegularUSer
        fields = ['username','full_name', 'email', 'phone', 'password1', 'password2']
        # full_name=forms.CharField(max_length=100, label="Name")
        # email=forms.EmailField(max_length=100, label="Name")
        # phone=forms.CharField(max_length=20, label="Name")

        def clean_username(self):
            username = self.cleaned_data['username']

            # Reject if username contains spaces
            if ' ' in username:
                raise ValidationError("Username cannot contain spaces.")

            # Reject if username already exists
            if RegularUSer.objects.filter(username=username).exists():
                raise ValidationError("This username is already taken.")

            return username



class RegularUSerLoginForm(AuthenticationForm):
    username = forms.EmailField(label='Email')
    class Meta:
        model = RegularUSer
        fields = ['email', 'password']