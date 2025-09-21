from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email','year','department','tools','purposes','accuracy']   # required
        widgets = {
            'purposes': forms.CheckboxSelectMultiple(),  # for multiple selection
        }
