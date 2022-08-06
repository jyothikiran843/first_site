from django.urls import reverse
from django.shortcuts import render,get_object_or_404
from django.views.generic import CreateView,DetailView,ListView,UpdateView,DeleteView
from blog.models import Article
from blog.forms import ArticleInput
# Create your views here.
class ArticleCreateView(CreateView):
    template_name= 'blog/article_create.html'
    form_class=ArticleInput
    queryset=Article.objects.all()

class ArticleUpdateView(UpdateView):
    template_name= 'blog/article_update.html'
    form_class=ArticleInput
    # queryset=Article.objects.all()
    def get_object(self):
        return get_object_or_404(Article,id=self.kwargs.get('id'))

class ArticleDeleteView(DeleteView):
    template_name='blog/article_delete.html'
    def get_object(self):
        return get_object_or_404(Article,id=self.kwargs.get('id'))
    
    def get_success_url(self):
        return reverse('blog_index')

class ArticleListView(ListView):
    queryset= Article.objects.all()

class ArticleDetailView(DetailView):
    template_name='blog/article_detail.html'
    def get_object(self):
        return get_object_or_404(Article,id=self.kwargs.get('id'))