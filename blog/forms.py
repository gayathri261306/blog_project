from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'author', 'content', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Title'}),
            'author': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Author'}),
            'content': forms.Textarea(attrs={'class': 'input-field', 'placeholder': 'Write your post...', 'rows':5}),
        }
