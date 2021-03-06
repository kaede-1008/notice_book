from django.contrib.auth.mixins import LoginRequiredMixin
from django_filters.views import FilterView
from django.urls import reverse_lazy
from django.views import generic

from .models import Post, Book
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
    template_name = 'apps/index.html'


class SearchView(generic.FormView):
    #success_url = reverse_lazy('polls:detail')
    form_class = SearchForm
    template_name = 'apps/search.html'
    
class SearchListView(generic.ListView):
    model = Book
    paginate_by = 5
    
    #Book.object.filter(Q(book_title__contains=self.request.title) | Q(book_auther__contains=self.request.auther) | Q(book_illust__contains=self.request.illust)).distinct()

    ordering = ['-book_title']
    template_name = 'apps/search_list.html'

    def get(self, request):
        title = request.GET.get("title")
        auther = request.GET.get("auther")
        illust = request.GET.get("illust")

        info = {
            'titles': title,
            'authers': auther,
            'illusts': illust,
        }

        return render(request, 'apps/search_list.html', info)
        
            


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