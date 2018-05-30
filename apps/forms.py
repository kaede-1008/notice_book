from django import forms
from .models import Book
class SearchForm(forms.Form):
    model = Book
    title = forms.CharField(required=False, max_length=100)
    auther = forms.CharField(required=False, max_length=100)
    illust = forms.CharField(required=False, max_length=100)

class Search_ListForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ("book_title", "book_auther", "book_illust")