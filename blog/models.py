from django.utils import timezone
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=timezone.now())
    image = models.ImageField(upload_to='blog_images/%Y/%m/%d/')