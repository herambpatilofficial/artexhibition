from django.contrib import admin
from .models import Category, Post,videoart,performances
# Register your models here.


admin.site.register(Category)
admin.site.register(Post)
admin.site.register(videoart)
admin.site.register(performances)