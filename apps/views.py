from django.contrib.auth.mixins import LoginRequiredMixin
from django_filters.views import FilterView
from django.urls import reverse_lazy
from django.views import generic

from apps.models import Post, Book
from django.shortcuts import render
from django.http.response import HttpResponse
from .forms import SearchForm
from django.shortcuts import redirect
from django.db.models import Q
# Create your views here.

class IndexView(generic.ListView):
    model = Post
    paginate_by = 5
    ordering = ['-publish_date']
    #success_url = reverse_lazy('apps:search')
    template_name = 'apps/index.html'


class SearchView(generic.FormView):
    #success_url = reverse_lazy('polls:detail')
    template_name = 'apps/search.html'
    form_class = SearchForm

    
class SearchListView(generic.ListView):
    form_class = SearchForm
    template_name = 'apps/search_list.html'

    def get_queryset(self):
        
        return Book.objects.all()

    
class DetailView(generic.DetailView):
    model = Book
    template_name = 'apps/details.html'

class CreateView(generic.edit.CreateView):
    model = Post
    fields = '__all__'
    template_name = 'apps/create.html'

class DeleteView(generic.edit.DeleteView):
    model = Post
    success_url = reverse_lazy('apps:index')
    template_name = 'apps/delete.html'