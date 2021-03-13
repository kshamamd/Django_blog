from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Appointment(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    appoint = models.ForeignKey(User, on_delete=models.CASCADE)
# Create your models here. appoint is a key


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    likes = models.ManyToManyField(User, default=None, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def num_likes(self):
        return self.likes.all().count()

#here we have to mention get absolute url of post


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=True)
    likes = models.ManyToManyField(User, blank=True, related_name='post_likes')

    def total_likes(self):
        return self.likes.count()

    def get_like_url(self):
        return reverse('post-likes', kwargs={'pk': self.pk})


class Task(models.Model):
    comment = models.CharField(max_length=300, default=None)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

