from django.urls import path, include
from .views import NewsListView, NewsCreateView, NewsDetailView
app_name = 'news'

urlpatterns = [
    path('', NewsListView.as_view(), name = 'list_news'),
    path('news/', NewsCreateView.as_view(), name='news' ),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='detail')
]
