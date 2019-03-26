from django import forms
from users.models import Player
from django.contrib.auth.models import User



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email','password')




class PlayerForm(forms.ModelForm):
    password = forms.CharField(label='Contrasena',widget=forms.PasswordInput)
    passwordConfirmation = forms.CharField(label='Repetir Contrasena', widget=forms.PasswordInput)

    class Meta:
        model = Player
        fields = ('name','last_names','date_of_birth','telephone','email_address','code','sex')
        widgets={'date_of_birth': forms.DateInput(attrs={'class': 'datepicker',
                                                         'placeholder':'format: mm/dd/yyyy'})

        }



    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] !=  cd ['passwordConfirmation']:
            raise forms.ValidationError('Passwords do not match')
        return cd ['passwordConfirmation']












