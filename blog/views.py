from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from .models import Blog
from django.views.generic import ListView
from .forms import BlogForm
from django.urls import reverse
from django.shortcuts import get_object_or_404

# Create your views here.
class BlogStart(ListView):
    template_name = 'blog/index.html'
    model = Blog
    context_object_name = 'posts'