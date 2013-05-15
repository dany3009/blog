from django.views.generic.simple import direct_to_template
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from django import forms
from django.contrib import auth
from blog.forms import *
import datetime

def home(request):
    posts = BlogPost.objects.all()
    return direct_to_template(request, 'home.html', { 'posts' : posts })

def about(request):
    return render(request, 'about.html')

@login_required
def contacts(request):
    subject = 'Mail from blog'
    message = request.POST.get('message', '')
    from_email = request.user.email
    if message:
        try:
            send_mail(subject, message, from_email, ['dany3009@rambler.ru'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/')
    else:
        return render_to_response('contacts.html', {'form': ContactForm()}, RequestContext(request))
    return render_to_response('contacts.html', {'form': ContactForm()}, RequestContext(request))

def register(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            user = auth.authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password1'])
            auth.login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = MyUserCreationForm()
    return render_to_response("register.html", { 'form' : form }, RequestContext(request))

def add_post(request):
    date = datetime.datetime.now()
    author = request.user.username
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return HttpResponseRedirect('/')
    else:
        form = BlogPostForm()
    return render_to_response("post_add.html", { 'form' : form, 'date' : date, 'author' : author }, RequestContext(request))

def view_post(request, post_id):
    post = BlogPost.objects.get(pk = post_id)
    return direct_to_template(request, 'view_post.html', { 'post' : post })

