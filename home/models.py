from django.forms import EmailField
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Permission
from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms



class UserCreationForm(UserCreationForm):
    email = EmailField(label=("Email address"), required=True, help_text=("Required."))
    is_superuser = models.BooleanField("IS SUPERUSER", default=False)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2","is_superuser")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

  