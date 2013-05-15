from django.db import models
from django.contrib import admin

class BlogPost(models.Model):
    title = models.CharField(max_length = 100)
    date = models.DateTimeField(auto_now_add = True)
    body = models.TextField()
    author = models.CharField(max_length = 100)
    
    class Meta():
        ordering = ["-date"]
    
    def __unicode__(self):
        return self.title
    
admin.site.register(BlogPost)