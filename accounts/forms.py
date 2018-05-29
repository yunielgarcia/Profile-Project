from django import forms
from django.contrib.auth.models import User
from accounts.models import UserProfile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('bio', 'picture', 'dob')


class UpdatePictureForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)
#   todo: subiendo un profile pic desde profile page

