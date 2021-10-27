from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import TextInput


class LoginForm(forms.Form):
    username =  forms.CharField(max_length=100 ,label="Username" , widget=forms.TextInput)
    password = forms.CharField(max_length=100,label="Password" , widget=forms.PasswordInput)


    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Not right username or password")
        return super(LoginForm, self).clean()


class RegisterForm(UserCreationForm):
    first_name =  forms.CharField(max_length=100 ,label="First Name" , widget=forms.TextInput(attrs={
        "placeholder":"First Name"
    }))
    last_name =  forms.CharField(max_length=100 ,label="Last Name" , widget=forms.TextInput)
    username =  forms.CharField(max_length=100 ,label="Username" , widget=forms.TextInput)
    email = forms.CharField(max_length=100, label="Email" , widget=forms.EmailInput())
    password1 = forms.CharField(max_length=100,label="Password" , widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=100,label="Confirn Password" , widget=forms.PasswordInput)

    class Meta:
            model = User
            fields = [
                'first_name',
                'last_name',
                'username',
                'email',
                'password1',
                'password2'
            ]

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Not same password")
        return password2
