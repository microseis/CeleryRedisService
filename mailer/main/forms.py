# coding=utf-8
from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'firstname': forms.TextInput(attrs={'placeholder': u'Иван'}),
            'lastname': forms.TextInput(
                attrs={'placeholder': u'Иванов'}),
            'email': forms.TextInput(
                attrs={'placeholder': u'example@mail.com'}),
            'dob': forms.TextInput(
                attrs={'placeholder': u'1990-12-11'}),
        }
