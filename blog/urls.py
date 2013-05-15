from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'blog.views.home', name='home'),
    url(r'^about/$', 'blog.views.about', name='about'),
    url(r'^contacts/$', 'blog.views.contacts', name='contacts'),
    
    url(r'^add_post/$', 'blog.views.add_post', name='add post'),
    url(r'^post/(?P<post_id>\d+)', 'blog.views.view_post', name='post view'),
    url(r'^comments/', include('django.contrib.comments.urls'), name='comments'),
    
    url( r'^login/$', 'django.contrib.auth.views.login', { "template_name": "login.html" }, name='login'),
    url( r'^logout/$', 'django.contrib.auth.views.logout', { "template_name": "logout.html" }, name='logout'),
    url( r'^register/$', 'blog.views.register', name='register'),
    
    url(r'^admin/', include(admin.site.urls)),
)
