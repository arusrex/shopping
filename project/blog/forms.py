from django import forms
from blog.models import CommentsNews, CommentsEvents
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.core.exceptions import ValidationError
import re

class CommentsNewsForm(forms.ModelForm):
    class Meta:
        model = CommentsNews
        fields = ['comment']
        widgets = {
            'comment': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escreva seu comentário aqui...',}),
        }

class CommentsEventsForm(forms.ModelForm):
    class Meta:
        model = CommentsEvents
        fields = ['comment']
        widgets = {
            'comment': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escreva seu comentário aqui...',}),
        }

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'given-name',}),
        label='Nome'
        )
    last_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'family-name',}),
        label='Sobrenome',
        )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'autocomplete': 'email',}),
        help_text="Digite um endereço de e-mail válido.",
        )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'username'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control',}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control',}),
        }
        labels = {
            'username': 'Usúario',
            'password1': 'Senha',
            'password2': 'Confirme a senha'
        }
        help_text = {
            'username': '150 caracteres ou menos. Letras, números e @/./+/-/_ apenas.',
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Nome de usuário'
        self.fields['username'].max_length = 10
        self.fields['password1'].label = 'Senha'
        self.fields['password2'].label = 'Confirme a senha'
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
            # if field.error_messages:
            #     field.widget.attrs.update({'class': 'form-control is-invalid'})
    
        
        
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        exist = User.objects.filter(email=email).exists()
        if exist:
            raise forms.ValidationError("Este e-mail já está cadastrado")
        return email
    

class CustomUserChangeForm(UserChangeForm):
    password = None
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome de usuário',}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome',}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sobrenome',}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail',}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        exist = User.objects.filter(email=email).exclude(pk=self.instance.pk).exists()
        if exist:
            raise ValidationError('Email já está em uso.')
        return email

class CustomPasswordChangeForm(PasswordChangeForm):

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2',)
        widgets = {
            'old_password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Senha antiga',}),
            'new_password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Nova senha', }),
            'new_password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Confirme a senha'}),
        }


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control',  'id': "floatingInput",}))
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': "floatingPassword",}))
