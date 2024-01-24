from django.urls import reverse_lazy
from datetime import datetime
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .filters import PostFilter
from .forms import PostForm
from django.shortcuts import render



class NewsList(ListView):
    model = Post
    ordering = '-created_at'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()

        page = context['page_obj']
        context['first_page'] = 1
        context['last_page'] = page.paginator.num_pages
        context['current_page'] = page.number
        context['pages_range'] = range(max(1, page.number - 1), min(page.paginator.num_pages + 1, page.number + 2))

        context['main_new'] = None
        return context

class NewsDetail(DetailView):
    model = Post
    template_name = 'new.html'
    context_object_name = 'new'

class NewsSearch(View):
    def get(self, request):
        filter = PostFilter(request.GET, queryset=Post.objects.all())
        return render(request, 'news_search.html', {'filter': filter})


class NewsCreate(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'news_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Создать новость'
        return context

    def get_success_url(self):
        return reverse_lazy('news_detail', kwargs={'pk': self.object.pk})

class ArticleCreate(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'article_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Создать статью'
        return context

class NewsUpdate(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'news_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Редактировать новость'
        return context

class ArticleUpdate(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'article_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = 'Редактировать статью'
        return context

class NewsDelete(DeleteView):
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news_list')

class ArticleDelete(DeleteView):
    model = Post
    template_name = 'article_delete.html'
    success_url = reverse_lazy('news_list')
