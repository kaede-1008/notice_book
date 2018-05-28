from django import forms
from .models import Book

class SearchForm(forms.ModelForm):
    class Meta:
        model = Book
        fields =['book_title', 'book_auther', 'book_illust']
