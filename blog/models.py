from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    
# Create your models here.
class Blog(models.Model):
    username = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    email = models.EmailField()
    text = models.TextField()
    image = models.ImageField(default= True)
    city = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=True)
    
    def __str__(self):
        return self.username
    
    


    
    