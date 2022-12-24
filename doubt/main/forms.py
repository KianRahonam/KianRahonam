from django import forms
from .models import UserAccount


class signUpform(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ("firstName","lastName","emailID","phoneNumber","status")