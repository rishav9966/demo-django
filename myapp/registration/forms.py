from django import forms
from django.core import validators
# custom validator 
def check_size(value):
    if len(value) < 6:
        raise forms.ValidationError("the password is too short")


class Signup(forms.Form):
    first_name = forms.CharField(initial='First Name', )
    last_name = forms.CharField(initial='Last Name', )
    email = forms.EmailField(help_text='Enter your Email', )
    Address = forms.CharField(required=False, )
    Technology = forms.CharField(initial = 'Django', disabled = True)
    age = forms.IntegerField()
    # password = forms.CharField(widget=forms.PasswordInput, validators=[validators.MinLengthValidator(6)])
    # custom validator as check_size defined above
    password = forms.CharField(widget=forms.PasswordInput, validators=[check_size, ])
    re_password = forms.CharField(help_text='reenter you password', widget=forms.PasswordInput, required=False)

    # validating password but not for professional 
    # another way is_valid is used in views.py but not professional
    # validation using validators are professional look above
    # def clean_password(self):
    #     password = self.cleaned_data['password']
    #     if len(password) < 4:
    #         raise forms.ValidationError("password too short")
    #     return password
    