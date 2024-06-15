from django import forms
from blog.models import CommentsNews, CommentsEvents, Category, Tag
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.core.exceptions import ValidationError
import re
from django.utils.safestring import mark_safe
from blog.models import Post, ImagesPost, News, ImageNew, Events, ImageEvent, Profile

class SiteConfig(forms.ModelForm):
    ...

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_image']
        widgets = {
            'profile_image': forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'image/*',})
        }
        labels = {
            'profile_image': 'Imagem do perfil',
        }
        

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

    def __init__(self, *args, **kwargs):
        text_username = mark_safe('<br>'.join([
            'Letras, números e @/./+/-/_ apenas.',
            'Mínimo 5 caracteres.',
            'Máximo 20 caracteres.',
        ]))

        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Nome de usuário'
        self.fields['username'].help_text = text_username
        self.fields['password1'].label = 'Senha'
        self.fields['password2'].label = 'Confirme a senha'
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
    
        
    def clean_username(self):
        username = self.cleaned_data.get('username')
        exist = User.objects.filter(username=username).exists()

        if exist:
            raise forms.ValidationError("Este nome de usuário já existe.")
            
        if len(username) < 5 or len(username) > 20: # type: ignore
            raise forms.ValidationError("O nome de usuário deve ter no mínimo 5 no máximo 20 caracteres.")
        
        for i in username: # type: ignore
            if i == ' ':
                raise forms.ValidationError("O nome de usuário não pode conter espaços.")

        return username

    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        exist = User.objects.filter(email=email).exists()
        if exist:
            raise forms.ValidationError("Este e-mail já está cadastrado")
        return email
    

class CustomUserChangeForm(UserChangeForm):
    password = None
    first_name = forms.CharField(
        min_length = 2,
        required = True,
        widget = forms.TextInput(attrs={'class': 'form-control'}),
        label = "Nome",
        )
    
    last_name = forms.CharField(
        min_length = 2,
        required=True,
        widget = forms.TextInput(attrs={'class': 'form-control',}),
        label = 'Sobrenome'
        )
    
    email = forms.EmailField(
        required=True,
        widget = forms.EmailInput(attrs={'class': 'form-control'})
        )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',)

    def clean_email(self):

        email = self.cleaned_data.get('email')


        if email != self.instance.email:
            exist = User.objects.filter(email=email).exclude(pk=self.instance.pk).exists()
            if exist:
                raise ValidationError('Email já está em uso.')
        return email

class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(CustomPasswordChangeForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})  


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control',  'id': "floatingInput",}))
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': "floatingPassword",}))


class NewPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'is_published': forms.CheckboxInput(attrs={'class': 'form-check-input',}),
            'title': forms.TextInput(attrs={'class': 'form-control',}),
            'short_description': forms.TextInput(attrs={'class': 'form-control',}),
            'description': forms.Textarea(attrs={'class': 'form-control',}),
            'number': forms.NumberInput(attrs={'class': 'form-control',}),
            'fone': forms.TextInput(attrs={'class': 'form-control',}),
            'whatsapp': forms.TextInput(attrs={'class': 'form-control',}),
            'email': forms.EmailInput(attrs={'class': 'form-control',}),
            'site': forms.URLInput(attrs={'class': 'form-control',}),
            'facebook': forms.URLInput(attrs={'class': 'form-control',}),
            'instagram': forms.URLInput(attrs={'class': 'form-control',}),
            'x_twitter': forms.URLInput(attrs={'class': 'form-control',}),
            'youtube': forms.URLInput(attrs={'class': 'form-control',}),
            'category': forms.Select(attrs={'class': 'form-select',}),
            'tags': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input mx-2',}),
        }
        labels = {
            'is_published': 'Publicado',
            'title': 'Título',
            'short_description': 'Descrição curta',
            'description': 'Descrição',
            'number': 'Número da loja',
            'fone': 'Telefone',
            'whatsapp': 'Whatsapp',
            'email': 'E-mail',
            'site': 'Site',
            'facebook': 'Facebook',
            'instagram': 'Instagram',
            'x_twitter': 'X (Antigo Twitter)',
            'youtube': 'Youtube',
            'cover': 'Imagem da Capa ou Logotipo',
            'category': 'Categoria',
            'tags': 'Tags',
        }
        help_texts = {
            'whatsapp': 'Digíte apenas números e o código da área, ex.: 00900000000',
        }

    def __init__(self, *args, **kwargs):
        super(NewPost, self).__init__(*args, **kwargs)
        self.fields["cover"].widget.attrs.update(
            {'class': 'form-control',
             'accept': 'image/*',
             }
        )
        
        self.fields['is_published'].label_suffix = ''


class NewImagesPost(forms.ModelForm):
    class Meta:
        model = ImagesPost
        fields = ['image',]
        widgets = {
            'image': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'accept': 'image/*',
                    'multiple': '',
                }
            ),
        }

class EditPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'is_published': forms.CheckboxInput(attrs={'class': 'form-check-input',}),
            'title': forms.TextInput(attrs={'class': 'form-control',}),
            'short_description': forms.TextInput(attrs={'class': 'form-control',}),
            'description': forms.Textarea(attrs={'class': 'form-control',}),
            'number': forms.NumberInput(attrs={'class': 'form-control',}),
            'fone': forms.TextInput(attrs={'class': 'form-control',}),
            'whatsapp': forms.TextInput(attrs={'class': 'form-control',}),
            'email': forms.EmailInput(attrs={'class': 'form-control',}),
            'site': forms.URLInput(attrs={'class': 'form-control',}),
            'facebook': forms.URLInput(attrs={'class': 'form-control',}),
            'instagram': forms.URLInput(attrs={'class': 'form-control',}),
            'x_twitter': forms.URLInput(attrs={'class': 'form-control',}),
            'youtube': forms.URLInput(attrs={'class': 'form-control',}),
            'category': forms.Select(attrs={'class': 'form-select',}),
            'tags': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input mx-2',}),
            'cover': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*', })
        }

class EditImagesPost(forms.ModelForm):
    class Meta:
        model = ImagesPost
        fields = ['image',]
        widgets = {
            'image': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'accept': 'image/*',
                    'multiple': '',
                }
            ),
        }


class AddNewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'
        widgets = {
            'is_published': forms.CheckboxInput(attrs={'class': 'form-check-input',}),
            'title': forms.TextInput(attrs={'class': 'form-control',}),
            'short_description': forms.TextInput(attrs={'class': 'form-control',}),
            'description': forms.Textarea(attrs={'class': 'form-control',}),
            'cover': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*', }),
            'cover_caption': forms.TextInput(attrs={'class': 'form-control',}),
        }
        labels = {
            'is_published': 'Publicação',
            'title': 'Título',
            'short_description': 'Curta descrição',
            'description': 'Descrição completa',
            'cover': 'Imagem da capa',
            'cover_caption': 'Texto da imagem da capa',
        }
        help_texts = {
            'is_published': 'Ativa ou Desativa a exibição',
            'short_description': 'Essa descrição aparece na tela inicial',
            'cover': 'Imagem que aparece como capa na tela inicial ',
        }

class AddImagesNewsForm(forms.ModelForm):
    class Meta:
        model = ImageNew
        fields = ['image',]
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*', 'multiple': '', }),
        }
        labels = {
            'image': 'Imagens',
        }

class EditNewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'
        widgets = {
            'is_published': forms.CheckboxInput(attrs={'class': 'form-check-input',}),
            'title': forms.TextInput(attrs={'class': 'form-control',}),
            'short_description': forms.TextInput(attrs={'class': 'form-control',}),
            'description': forms.Textarea(attrs={'class': 'form-control',}),
            'cover': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*', }),
            'cover_caption': forms.TextInput(attrs={'class': 'form-control',}),
        }
        labels = {
            'is_published': 'Publicação',
            'title': 'Título',
            'short_description': 'Curta descrição',
            'description': 'Descrição completa',
            'cover': 'Imagem da capa',
            'cover_caption': 'Texto da imagem da capa',
        }
        help_texts = {
            'is_published': 'Ativa ou Desativa a exibição',
            'short_description': 'Essa descrição aparece na tela inicial',
            'cover': 'Imagem que aparece como capa na tela inicial ',
        }


class AddEventsForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = '__all__'
        widgets = {
            'is_published': forms.CheckboxInput(attrs={'class': 'form-check-input',}),
            'title': forms.TextInput(attrs={'class': 'form-control',}),
            'short_description': forms.TextInput(attrs={'class': 'form-control',}),
            'description': forms.Textarea(attrs={'class': 'form-control',}),
            'cover': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*', }),
            'cover_caption': forms.TextInput(attrs={'class': 'form-control',}),
        }
        labels = {
            'is_published': 'Publicação',
            'title': 'Título',
            'short_description': 'Curta descrição',
            'description': 'Descrição completa',
            'cover': 'Imagem da capa',
            'cover_caption': 'Texto da imagem da capa',
        }
        help_texts = {
            'is_published': 'Ativa ou Desativa a exibição',
            'short_description': 'Essa descrição aparece na tela inicial',
            'cover': 'Imagem que aparece como capa na tela inicial ',
        }

class AddImagesEventsForm(forms.ModelForm):
    class Meta:
        model = ImageEvent
        fields = ['image',]
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*', 'multiple': '', }),
        }
        labels = {
            'image': 'Imagens',
        }

class EditEventsForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = '__all__'
        widgets = {
            'is_published': forms.CheckboxInput(attrs={'class': 'form-check-input',}),
            'title': forms.TextInput(attrs={'class': 'form-control',}),
            'short_description': forms.TextInput(attrs={'class': 'form-control',}),
            'description': forms.Textarea(attrs={'class': 'form-control',}),
            'cover': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*', }),
            'cover_caption': forms.TextInput(attrs={'class': 'form-control',}),
        }
        labels = {
            'is_published': 'Publicação',
            'title': 'Título',
            'short_description': 'Curta descrição',
            'description': 'Descrição completa',
            'cover': 'Imagem da capa',
            'cover_caption': 'Texto da imagem da capa',
        }
        help_texts = {
            'is_published': 'Ativa ou Desativa a exibição',
            'short_description': 'Essa descrição aparece na tela inicial',
            'cover': 'Imagem que aparece como capa na tela inicial ',
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name',]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',}),
        }
        labels = {
            'name': 'Nome da Categoria',
        }

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name',]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',}),
        }
        labels ={
            'name': 'Nome da Tag',
        }
