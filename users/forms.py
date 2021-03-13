from django import forms
from django.core import validators
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import New, Status, Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    number = forms.IntegerField()

    class Meta:
        model = User
        fields = ['username', 'email', 'number', 'password1', 'password2']


class NewForm(forms.ModelForm):

    class Meta:
        model = New
        fields = ['name', 'surname', 'role', 'number', 'date', 'optional_number', 'address', 'reason']


class StatusCheck(forms.ModelForm):
    remark = forms.CharField()

    class Meta:
        model = Status
        fields = ['status', 'remark']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    number = forms.IntegerField()

    class Meta:
        model = User
        fields = ['username', 'email', 'number']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

