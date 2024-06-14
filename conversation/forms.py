from django import forms
from .models import Contacts, Messages


class AddContactForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ('name', 'contact_user')


class AddMessageForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ('message', 'picture', 'audio', 'video', 'docs')