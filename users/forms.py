from django import forms
from django.forms import CharField, ModelForm, PasswordInput

from . import models


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = models.Users
        fields = ['username', 'bio', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class EditProfileForm(ModelForm):
    password = CharField(widget=PasswordInput)

    class Meta:
        model = models.Users
        fields = ['username', 'bio', 'password', 'image']
