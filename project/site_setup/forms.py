from django import forms
from django.core.exceptions import ValidationError
from site_setup.models import SiteSetup
from django_summernote.widgets import SummernoteWidget

class SiteSetupForm(forms.ModelForm):
    class Meta:
        model = SiteSetup
        fields = '__all__'
        widgets = {
            'show_title': forms.CheckboxInput(attrs={'class':'form-check-input',}),
            'title': forms.TextInput(attrs={'class':'form-control',}),
            'show_logo': forms.CheckboxInput(attrs={'class':'form-check-input',}),
            # 'favicon': forms.FileInput(attrs={'class':'form-control', 'accept': 'image/*',}),
            # 'logo': forms.FileInput(attrs={'class':'form-control', 'accept': 'image/*',}),
            'description': SummernoteWidget(),
            'title_welcome_banner': forms.TextInput(attrs={'class':'form-control',}),
            'show_welcome_banner': forms.CheckboxInput(attrs={'class':'form-check-input',}),
            'welcome_banner': SummernoteWidget(),
            'title_best_banner': forms.TextInput(attrs={'class':'form-control',}),
            'show_best_banner': forms.CheckboxInput(attrs={'class':'form-check-input',}),
            'best_banner': SummernoteWidget(),
            'link_best_banner': forms.TextInput(attrs={'class':'form-control',}),
            'title_history_banner': forms.TextInput(attrs={'class':'form-control',}),
            'show_history_banner': forms.CheckboxInput(attrs={'class':'form-check-input',}),
            'history_banner': SummernoteWidget(),
            'link_history_banner': forms.TextInput(attrs={'class':'form-control',}),
            # 'img_history': forms.FileInput(attrs={'class':'form-control', 'accept': 'image/*',}),
            'show_operate_shop': forms.CheckboxInput(attrs={'class':'form-check-input',}),
            'operate_time_shop': SummernoteWidget(),
            'show_operate_food': forms.CheckboxInput(attrs={'class':'form-check-input',}),
            'operate_time_food': SummernoteWidget(),
            'show_social': forms.CheckboxInput(attrs={'class':'form-check-input',}),
            'facebook': forms.TextInput(attrs={'class':'form-control',}),
            'instagram': forms.TextInput(attrs={'class':'form-control',}),
            'x_twitter': forms.TextInput(attrs={'class':'form-control',}),
            'youtube': forms.TextInput(attrs={'class':'form-control',}),
            'show_login': forms.CheckboxInput(attrs={'class':'form-check-input',}),
            'show_header': forms.CheckboxInput(attrs={'class':'form-check-input',}),
            'show_footer': forms.CheckboxInput(attrs={'class':'form-check-input',}),
            'show_search': forms.CheckboxInput(attrs={'class':'form-check-input',}),
            'show_menu': forms.CheckboxInput(attrs={'class':'form-check-input',}),
            'show_pagination': forms.CheckboxInput(attrs={'class':'form-check-input',}),
            'show_subscribe': forms.CheckboxInput(attrs={'class':'form-check-input',}),
            'show_comments': forms.CheckboxInput(attrs={'class':'form-check-input',}),
            'show_news': forms.CheckboxInput(attrs={'class':'form-check-input',}),
            'show_events': forms.CheckboxInput(attrs={'class':'form-check-input',}),
            'show_carousel': forms.CheckboxInput(attrs={'class':'form-check-input',}),
            'slide1_title': forms.TextInput(attrs={'class':'form-control',}),
            'slide2_title': forms.TextInput(attrs={'class':'form-control',}),
            'slide3_title': forms.TextInput(attrs={'class':'form-control',}),
            'slide1_description': forms.TextInput(attrs={'class':'form-control',}),
            'slide2_description': forms.TextInput(attrs={'class':'form-control',}),
            'slide3_description': forms.TextInput(attrs={'class':'form-control',}),
            # 'slide1': forms.FileInput(attrs={'class':'form-control', 'accept': 'image/*',}),
            # 'slide2': forms.FileInput(attrs={'class':'form-control', 'accept': 'image/*',}),
            # 'slide3': forms.FileInput(attrs={'class':'form-control', 'accept': 'image/*',}),

        }
        labels = {
            'show_title': 'Mostrar o título',
            'title': 'Título',
            'show_logo': 'Mostrar logo',
            'logo': 'Logo',
        }