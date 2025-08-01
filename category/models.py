from django.db import models

# Create your models here.

class Category(models.Model):
    category_name=models.CharField(max_length=60)
    slug=models.CharField(max_length=60)
    description=models.TextField(max_length=120,blank=True)
    cat_image=models.ImageField(upload_to="images/",blank=True)
    
    class Meta:
       verbose_name='Category'
       verbose_name_plural='Categories'
    def __str__(self):
     return self.category_name
     