from django import forms
from users.models import Player




class PlayerForm(forms.ModelForm):
    password = forms.CharField(label='Contrasena',widget=forms.PasswordInput)
    passwordConfirmation = forms.CharField(label='Repetir Contrasena', widget=forms.PasswordInput)

    class Meta:
        model = Player
        fields = ('name','last_names','date_of_birth','telephone','email_address','code')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] !=  cd ['passwordConfirmation']:
            raise forms.ValidationError('Passwords do not match')
        return cd ['passwordConfirmation']












