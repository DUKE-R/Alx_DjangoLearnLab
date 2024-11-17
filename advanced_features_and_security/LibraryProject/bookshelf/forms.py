from django import forms

class BookSearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False)

from django import forms

class BookForm(forms.Form):
    title = forms.CharField(max_length=200)
    author = forms.CharField(max_length=100)
    published_date = forms.DateField()

from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']

    # Optionally, you can add custom validation here if needed
    def clean_title(self):
        title = self.cleaned_data['title']
        # Example of a simple validation: ensuring title is not empty
        if not title:
            raise forms.ValidationError("Title is required.")
        return title
