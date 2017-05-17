from django import forms


class RegisterForm(forms.Form):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    email = forms.EmailField(label='Your Email Address')
    date_of_birth = forms.DateField(label='Date of Birth')
    password = forms.PasswordInput()
    password2 = forms.PasswordInput()
