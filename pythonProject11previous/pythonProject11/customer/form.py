from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm as forms

class UserRegistrationForm(forms):
    email=forms.Email.Field()
    first_Name=forms.CharField(max_length=10)
    last_Name = forms.CharField(max_length=10)

class Meta:
    model=User
    fields=[
        'username',
        'email',
        'first_Name',
        'last_Name',
        'password',
        'confirm_password',
    ]