import datetime

from django import forms
from django.contrib.auth.models import User
from accounts.models import UserProfile
from django.contrib.auth.password_validation import validate_password


def general_validation(value):
    if not validate_password(value):
        forms.ValidationError('Password is not valid')


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(),
                               validators=[general_validation])

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')


class UserProfileForm(forms.ModelForm):
    dob = forms.DateTimeField(input_formats=[
        '%Y-%m-%d',
        '%m/%d/%Y',
        '%m/%d/%y'],
        widget=forms.DateTimeInput(format='%m/%d/%Y'))

    class Meta:
        model = UserProfile
        fields = ('bio', 'picture', 'dob')


class UpdatePictureForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)


class EditUserForm(forms.ModelForm):
    confirm_email = forms.CharField(label='Confirm Email')

    class Meta:
        model = User
        fields = ('email', 'confirm_email', 'first_name', 'last_name')

    def clean(self):
        """Cleans the entire form"""
        clean_data = super().clean()
        email = clean_data.get('email')
        verify = clean_data.get('confirm_email')

        if email != verify:
            raise forms.ValidationError("You need to enter the same email in both fields")
