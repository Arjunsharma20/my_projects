from django.db import models
# from .forms import PasswordInput
from django.contrib.auth.hashers import make_password

class LoginInfo(models.Model):
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=12)

    def __str__(self):
        return self.name

    # def set_password(self,raw_password):
    #     self.password= make_password(raw_password)

    def check_password(self,raw_password):
        from django.contrib.auth.hashers import check_password
        return check_password(raw_password,self.password)

class RegisterInfo(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
    confirm_password = models.CharField(max_length=15)

    def __str__(self):
        return self.name

    def set_password(self,raw_password):
        self.password= make_password(raw_password)

    def check_password(self,raw_password):
        from django.contrib.auth.hashers import check_password
        return check_password(raw_password,self.password)
# Create your models here.

