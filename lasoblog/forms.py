from django import forms
from .models import Newblog

class NewBlogForm(forms.ModelForm):
    class Meta:
        model = Newblog
        fields = ['name', 'blog', 'blogTitle', 'blogimage']  # Fields to display in the form

class BlogForm(forms.ModelForm):
    class Meta:
        model = Newblog
        fields = ['name', 'blog', 'blogTitle', 'blogimage']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'blog': forms.Textarea(attrs={'class': 'form-control'}),
            'blogTitle': forms.TextInput(attrs={'class': 'form-control'}),
            'blogimage': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }