from django.shortcuts import render
from django.views.generic import ListView
from .models import import Post

class NewsList(ListView)
    model = Post
    ordering = 'title'
    template_name = 'news.html'
    context_object_name = 'news'


# Create your views here.
