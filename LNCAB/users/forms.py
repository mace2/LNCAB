from django import forms
from users.models import Player
from django.contrib.auth.models import User




class UserForm(forms.ModelForm):
    password = forms.CharField(label='Password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password')


    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] !=  cd ['password2']:
            raise forms.ValidationError('Passwords do not match')
        return cd ['passwordConfirmation']



class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        default= User.objects.filter().order_by('-id')[:1]
        fields = ('id_User','date_of_birth','telephone','code','sex')#checar code
        widgets={'date_of_birth': forms.DateInput(attrs={'class': 'datepicker',
                                                         'placeholder':'format: mm/dd/yyyy'}),



                  #  'id_User' : forms.CharField(attrs={'placeholder':'Username'})
        }














