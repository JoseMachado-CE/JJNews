from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from .models import Blog
from django.views.generic import ListView, DetailView, TemplateView
from .forms import BlogForm
from django.urls import reverse
from django.shortcuts import get_object_or_404


class BlogStart(ListView):
    template_name = 'blog/index.html'
    model = Blog
    context_object_name = 'posts'
    

class PostSingle(DetailView):
    template_name = 'blog/post_ind.html'
    model = Blog
    context_object_name = 'posts'
    

        

            
        
        
    
    
    
    
        
    
    

