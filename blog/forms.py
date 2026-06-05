from django import forms
from .models import Post, Categoria


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'resumen', 'contenido', 'categoria', 'archivo']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Título del post'
            }),
            'resumen': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Breve descripción (opcional, máx. 300 caracteres)'
            }),
            'contenido': forms.Textarea(attrs={
                'class': 'form-textarea',
                'placeholder': 'Contenido del post'
            }),
            'categoria': forms.Select(attrs={
                'class': 'form-input'
            }),
        }
