from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomLoginForm(AuthenticationForm):
    account_type = forms.CharField(max_length=50, required=False)
