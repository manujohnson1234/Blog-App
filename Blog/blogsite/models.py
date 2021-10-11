from django.db import models

from django.urls import reverse
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blogs')


class Post(models.Model):
    title = models.CharField(max_length=200)
    title_tag = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(null=True, blank=True)
    posted = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=200, default='none')
    snippets = models.CharField(max_length=300)
    likes = models.ManyToManyField(User, related_name='blog_post')
    images = models.ImageField(null=True, blank=True, upload_to='images/')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('blog', args=(str(self.id)))

    """
        @property
        def imageURL(self):
            try:
                url = self.images.url
            except:
                url = ''
    
            return url
    """