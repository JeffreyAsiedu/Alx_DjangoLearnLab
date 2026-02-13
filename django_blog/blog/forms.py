from django import forms
from .models import Post, Comment
from taggit.forms import TagWidget()


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content'] 
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Write your comment here...',
                'class': 'form-control'
            }),
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'tags': TagWidget(attrs={
                'class': 'tag-input',
                'placeholder': 'Add tags separated by commas'
            }),
        }
