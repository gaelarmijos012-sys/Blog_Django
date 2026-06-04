from django import forms
from .models import Post

class postForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'contenido']
        widgets = {
            'titulo': forms.TextInput(attrs={'class':'form-input', 'placeholder': 'Titulo del Post'}),
            'contenido': forms.Textarea(attrs={'class':'form-textarea','placeholder': 'Contenido del Post'})
        }