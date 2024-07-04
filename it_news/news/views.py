from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, DeleteView
from django.urls import reverse_lazy, reverse

from .models import News

class NewsListView(ListView):
    model = News
    ordering = 'id'
    paginate_by = 20
    template_name = 'news/list_news.html'


class NewsCreateView(CreateView):
    model = News
    fields = '__all__'
    template_name = 'news/create_news.html'


    def get_success_url(self):
        return reverse_lazy('news:detail', kwargs={'pk': self.object.pk})


class NewsDetailView(DetailView):
    model = News
    template_name = 'news/detail.html'


class NewsDeleteView(DeleteView):
    model = News
    template_name = 'news/delete.html'
    success_url = reverse_lazy('news:list_news')