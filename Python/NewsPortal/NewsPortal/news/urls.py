from django.urls import path
from .views import NewsList, NewsDetail, NewsSearch, NewsCreate, ArticleCreate, NewsUpdate, ArticleUpdate, NewsDelete, ArticleDelete

urlpatterns = [
    path('news/create/', NewsCreate.as_view(), name='news_create'),
    path('news/<int:pk>/edit/', NewsUpdate.as_view(), name='news_update'),
    path('news/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
    path('articles/create/', ArticleCreate.as_view(), name='article_create'),
    path('articles/<int:pk>/edit/', ArticleUpdate.as_view(), name='article_update'),
    path('articles/<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),
    path('news/', NewsList.as_view(), name='news_list'),
    path('news/search/', NewsSearch.as_view(), name='news_search'),
    path('news/<int:pk>', NewsDetail.as_view(), name='news_detail'),
]
