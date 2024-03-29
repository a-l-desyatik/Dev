from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):
        # Рейтинг постов (умноженный на 3)
        post_rating = self.post_set.aggregate(post_rating=Sum('rating')).get('post_rating') * 3

        # Рейтинг комментариев автора
        comment_rating = self.user.comment_set.aggregate(comment_rating=Sum('rating')).get('comment_rating')

        # Рейтинг комментариев к постам автора
        comment_post_rating = Comment.objects.filter(post__author=self).aggregate(comment_post_rating=Sum('rating')).get('comment_post_rating')

        # Обновление рейтинга автора
        self.rating = (post_rating or 0) + (comment_rating or 0) + (comment_post_rating or 0)
        self.save()

 class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    NEWS = 'NW'
    ARTICLE = 'AR'
    POST_TYPE_CHOICES = [
        (NEWS, 'News'),
        (ARTICLE, 'Article'),
    ]
    post_type = models.CharField(max_length=2, choices=POST_TYPE_CHOICES, default=ARTICLE)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.text[:124] + '...'

    def __str__(self):
        return self.name.title()

class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
