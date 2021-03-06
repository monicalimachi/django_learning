from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.views.generic import(
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

from .models import Article

class ArticleListView(ListView):
    template_name='articles/article_list.html'
    queryset=Article.objects.all()

class ArticleDetailView(DetailView):
    template_name='articles/article_detail.html'
    #queryset=Article.objects.all()

    def get_object(self):
        id_=self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)