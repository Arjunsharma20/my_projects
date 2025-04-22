from django import forms
from django.contrib.auth.hashers import check_password
from django.shortcuts import redirect
# from .views import user
from .models import LoginInfo
from .models import RegisterInfo

class LoginForm(forms.Form):


    username = forms.CharField(max_length=15)
    password = forms.CharField(widget=forms.PasswordInput)
    # confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username= self.cleaned_data['username']
        if not RegisterInfo.objects.filter(username=username).exists():
            raise forms.ValidationError("username does not exist")
        return username
        
    # def clean_password(self):
    #     # password = self.cleaned_data['password']
    #     user =
    #     if check_password(password,user.password):
    #         return redirect()

    #     return password
        
class RegisterForm(forms.Form):
    name = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=50)
    
    username = forms.CharField(max_length=15)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean_email(self):
        email =self.cleaned_data['email']
        if RegisterInfo.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already Reguster")
        
        return email
    
    def clean_username(self):
        username= self.cleaned_data['username']
        if RegisterInfo.objects.filter(username=username).exists():
            raise forms.ValidationError("username exist")
        
        return username
        
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password and confirm_password and password !=confirm_password:
            raise forms.ValidationError("Password does not match")
