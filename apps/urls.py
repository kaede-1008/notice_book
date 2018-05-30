
from django.urls import path
from . import views
from .forms import SearchForm

app_name ='apps'

urlpatterns = [
     # 一覧表示のURL: /
    path('', views.IndexView.as_view(), name='index'),  # url is /
 
    # 新規作成のURL: /post/create/
    path('post/create/', views.CreateView.as_view(), name='create'),
 
    path('search/', views.SearchView.as_view(form_class=SearchForm), name='search'),

    path('search_list/', views.SearchListView.as_view(), name='search_list'),
    # 以下では記事IDを 123 とします
    # 詳細表示のURL: /post/123/
    path('post/<int:pk>/', views.DetailView.as_view(), name='detail'),
    
    # 記事削除のURL: /post/123/delete/
    path('post/<int:pk>/delete/', views.DeleteView.as_view(), name='delete'),
]