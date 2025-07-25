from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']


class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, strip=True)