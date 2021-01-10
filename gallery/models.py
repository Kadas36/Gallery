from django.db import models
import datetime as dt

# Create your models here.

class location(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']    

class Category(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name   

    class Meta:
        ordering = ['name'] 

class Image(models.Model):
    image = models.ImageField(upload_to = 'gallery/')
    name = models.CharField(max_length=30)
    url = models.TextField()
    description = models.TextField(blank=True)
    location = models.ForeignKey('location', on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    date_posted = models.DateTimeField(auto_now=True) 

    class Meta:
        ordering = ['date_posted']   

    def __str__(self):
        return self.name                       