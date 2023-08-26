from django.db import models
from django.forms import ModelForm
from django.forms.fields import CharField
from ckeditor.widgets import CKEditorWidget
# Create your models here.

class Blogsite(models.Model):
    title= models.CharField(max_length=100)
    img= models.ImageField(upload_to='pics')
    desc= models.TextField()
    author = models.TextField(max_length=50, null= False, default = 'Suman')
    date  = models.DateField(auto_now=True)
    theme = models.TextField(max_length=100, default='Enter the theme of the Blog in 100 words')


# class BlogUser(ModelForm):
#     body = CharField(widget=CKEditorWidget())

#     class Meta:
#         model= Blogsite
#         fields = ['title','body', 'author']


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title