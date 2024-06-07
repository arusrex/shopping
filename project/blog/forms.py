from django import forms
from blog.models import CommentsNews, CommentsEvents

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
