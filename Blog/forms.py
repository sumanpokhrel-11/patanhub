from django import forms
from tinymce import TinyMCE
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'col':80, 'row':30}))
    
    class Meta:
        model = BlogPost
        fields = ['title', 'content']
