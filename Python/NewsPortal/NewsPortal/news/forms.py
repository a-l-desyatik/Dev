from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'title', 'text', 'category', 'rating']

class SearchForm(forms.Form):
    title = forms.CharField(required=False, label='Название')
    author = forms.CharField(required=False, label='Автор')
    date_from = forms.DateField(required=False, label='Дата с', widget=forms.SelectDateWidget)
