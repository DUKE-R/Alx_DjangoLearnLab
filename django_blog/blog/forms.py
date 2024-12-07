from .models import Post
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from taggit.forms import TagWidget
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Enter a valid email address.")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    class PostForm(forms.ModelForm):
       tags = forms.CharField(required=False, help_text="Add tags separated by commas")
       class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'tags': TagWidget()
        }

        def save(self, commit=True):
         instance = super().save(commit=False)
         tag_names = [tag.strip() for tag in self.cleaned_data['tags'].split(',') if tag]
         if commit:
            instance.save()
            instance.tags.set([Tag.objects.get_or_create(name=tag)[0] for tag in tag_names])
         return instance
        
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Enter your comment here...'}),
        }

