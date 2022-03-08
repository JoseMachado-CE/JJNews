from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogStart.as_view()),
]