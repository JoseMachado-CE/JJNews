from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogStart.as_view(), name="Blogstart"),
    path('blog/<slug:slug>/', views.PostSingle.as_view(), name="post-single"),
    path('favorite', views.PostsFavorite, name='read-later')
]