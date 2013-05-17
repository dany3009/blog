from django.db import models
from django.contrib import admin
from tinymce.models import HTMLField

class BlogPost(models.Model):
    title = models.CharField(max_length = 100)
    date = models.DateTimeField(auto_now_add = True)
    body = HTMLField()
    author = models.CharField(max_length = 100)
    
    class Meta():
        ordering = ["-date"]
    
    def __unicode__(self):
        return self.title
    
admin.site.register(BlogPost)