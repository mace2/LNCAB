from django import forms
from users.models import Player
from tournaments.models import Team
from teams.models import Sex
from django.db import models

from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords do not match')
        return cd['password2']


class PlayerForm(forms.Form):
    code = forms.CharField(max_length=100)
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker',
                                                                  'placeholder': 'format: mm/dd/yyyy'}))
    telephone = forms.CharField(max_length=100)
    sex = forms.ModelChoiceField(queryset=Sex.objects.all())

    def clean(self):
        cleaned_data = super().clean()
        code = cleaned_data.get("code")
        if code:
            try:
                Team.objects.get(code=code)
            except Team.DoesNotExist:
                raise forms.ValidationError("No team has this code")


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
