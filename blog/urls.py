from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogStart.as_view(), name="Blogstart"),
    path('<slug:slug>/', views.PostSingle.as_view(), name="post-single")  
]