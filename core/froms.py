from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from core.models import Contact

class ContactUsForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ("email", "name", "subject", "message")
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }

from django import forms
from core.models import Contact




# class ContactUsForm(forms.ModelForm):

#     class Meta:
#         model = Contact
#         fields = ("email", "name", "subject", "message")


     