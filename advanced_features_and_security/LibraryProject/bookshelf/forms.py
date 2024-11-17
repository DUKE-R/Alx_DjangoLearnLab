from django import forms

class BookSearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False)

from django import forms

class BookForm(forms.Form):
    title = forms.CharField(max_length=200)
    author = forms.CharField(max_length=100)
    published_date = forms.DateField()
