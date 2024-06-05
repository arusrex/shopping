from django import forms
from blog.models import Category

class CategoryFilter(forms.Form):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False, label='Categorias')