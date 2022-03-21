from django.db import models
from django.utils.text import slugify

class Author(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    
# Create your models here.
class Blog(models.Model):
    username = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    slug = models.SlugField(primary_key=True, db_index=True)
    email = models.EmailField()
    text = models.TextField()
    post_data = models.DateTimeField(auto_now_add=True)
    pre_text = models.CharField(max_length=250)
    image = models.ImageField(upload_to='posts', null=True)
    city = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=True)
        
        
    def __str__(self):
        return self.username
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        


class all_products(models.Model):
    def get_all_products():
        items = []
        with open('/flipkart_com-ecommerce_sample.csv','r') as fp:
            # You can also put the relative path of csv file
            # with respect to the manage.py file
            reader1 = csv.reader(fp, delimiter=';')
            for value in reader1:
                items.append(value)
                
        return items
        print(items)
    
    


    
    