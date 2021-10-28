from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import TextInput


class LoginForm(forms.Form):
    username =  forms.CharField(max_length=100 ,label="Username" , widget=forms.TextInput(attrs={
        "placeholder":"Username"
    }))
    password = forms.CharField(max_length=100,label="Password" , widget=forms.PasswordInput(attrs={
        "placeholder":"Password"
    }))


    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Not right username or password")
        return super(LoginForm, self).clean()


class RegisterForm(UserCreationForm):
    username =  forms.CharField(max_length=100 ,label="Username" , widget=forms.TextInput(attrs={
        "placeholder":"Username"
    }))
    email = forms.CharField(max_length=100, label="Email" , widget=forms.EmailInput(attrs={
        "placeholder":"Email"
    }))
    password1 = forms.CharField(max_length=100,label="Password" , widget=forms.PasswordInput(attrs={
        "placeholder":"Password"
    }))
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={
        "placeholder":"Confirm Password"
    }))

    class Meta:
            model = User
            fields = [
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
