from django import forms
from django.core.exceptions import ValidationError
from site_setup.models import SiteSetup

class SiteSetupForm(forms.ModelForm):
    class Meta:
        model = SiteSetup
        fields = '__all__'
        widgets = {
            'show_title': forms.CheckboxInput(attrs={'class':'form-check-input',}),
            'title': forms.TextInput(attrs={'class':'form-control',}),
            'show_logo': forms.CheckboxInput(attrs={'class':'form-check-input',}),
            'logo': forms.FileInput(attrs={'class':'form-control', 'accept': 'image/*',}),
        }
        labels = {
            'show_title': 'Mostrar o título',
            'title': 'Título',
            'show_logo': 'Mostrar logo',
            'logo': 'Logo',
        }