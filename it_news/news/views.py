from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy, reverse

from .models import News

class NewsListView(ListView):
    model = News
    ordering = 'id'
    paginate_by = 10
    template_name = 'news/list_news.html'


class NewsCreateView(CreateView):
    model = News
    fields = '__all__'
    template_name = 'news/create_news.html'
    #success_url = reverse_lazy('news:detail')

    def news(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().news(request, *args, **kwargs)

    def get_success_url(self):
        news = self.get_object()
        return reverse_lazy('news:detail', kwargs={'pk': news.pk})


class NewsDetailView(DetailView):
    model = News
    template_name = 'news/detail.html'