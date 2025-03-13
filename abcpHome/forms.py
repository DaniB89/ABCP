# abcpHome/forms.py

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import UserProfile

class CombinedForm(forms.Form):
    login_username = forms.CharField(label='Username', max_length=100, required=False)
    login_password = forms.CharField(label='Password', widget=forms.PasswordInput, required=False)
    register_email = forms.EmailField(label='Email', required=False)
    register_username = forms.CharField(label='Username', max_length=100, required=False)
    register_password1 = forms.CharField(label='Password', widget=forms.PasswordInput, required=False)
    register_password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput, required=False)

    def clean(self):
        cleaned_data = super().clean()
        login_username = cleaned_data.get('login_username')
        login_password = cleaned_data.get('login_password')
        register_email = cleaned_data.get('register_email')
        register_password1 = cleaned_data.get('register_password1')
        register_password2 = cleaned_data.get('register_password2')

        if login_username and login_password:
            return cleaned_data

        if register_email and register_password1 and register_password2:
            if register_password1 != register_password2:
                self.add_error('register_password2', "Passwords do not match")
            return cleaned_data

        raise forms.ValidationError("Please fill out either the login or registration fields.")


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_pic', 'bio']

