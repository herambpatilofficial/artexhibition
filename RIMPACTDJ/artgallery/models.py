from django.db import models
from django.utils.html import format_html
# Create your models here.
class Category(models.Model):
    catId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    artistname = models.CharField(max_length=200)
    image = models.ImageField(upload_to='Media/artworks/')

    def __str__(self):
        return self.title

    def img_tag(self):
        return format_html('<img src="{}" width="150" height="150" />'.format(self.image.url))

class Post(models.Model):
    postId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    artist = models.TextField()
    image = models.ImageField(upload_to='Media/postartworks/')
    socialLink = models.URLField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class videoart(models.Model):
    videoId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    artist = models.TextField()
    videoLink = models.URLField(max_length=200)
    socialLink = models.URLField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class performances(models.Model):
    performanceId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    artist = models.TextField()
    performlink = models.URLField(max_length=200)
    socialLink = models.URLField(max_length=200)
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE)