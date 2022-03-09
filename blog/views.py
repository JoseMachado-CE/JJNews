from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import Blog

# Create your views here.
class BlogStart(View):
    def get(self, request):
        posts = Blog.objects.all()
        context = {
            'posts': posts
        }
        return render(request, 'blog/index.html', context)
    
    
    