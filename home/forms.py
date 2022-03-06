from distutils.command.build_scripts import first_line_re
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

UserModel = get_user_model()


class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Enter password', 
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', 
                                widget=forms.PasswordInput)
    class Meta:
        model = UserModel
        fields = ["username", "password1", "password2"]
        help_texts={
            'username':None
        }