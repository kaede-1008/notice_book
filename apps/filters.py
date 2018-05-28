from django_filters import filters
from django_filters import FilterSet
from .models import Book


class MyOrderingFilter(filters.OrderingFilter):
    descending_fmt = '%s (降順) '

class BookFilter(FilterSet):

    book_title = filters.CharFilter(name='book_title', label='題名', lookup_expr='contains')
    book_auther = filters.CharFilter(name='book_auther', label='著者', lookup_expr='contains')
    book_illust = filters.CharFilter(name='book_illust', label='イラストレーター', lookup_expr='contains')

    class Meta:
        model = Book
        fields = {'book_title', 'book_auther', 'book_illust',}
        