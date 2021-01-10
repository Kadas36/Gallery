from django.db import models
import datetime as dt

# Create your models here.

class location(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name'] 

    def save_location(self):
        self.save()
       

class Category(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name   

    class Meta:
        ordering = ['name'] 

    def save_category(self):
        self.save()
    

class Image(models.Model):
    image = models.ImageField(upload_to = 'gallery/')
    name = models.CharField(max_length=30)
    url = models.TextField()
    description = models.TextField(blank=True)
    location = models.ForeignKey('location', on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    date_posted = models.DateTimeField(auto_now_add=True) 

    class Meta:
        ordering = ['date_posted']   

    def __str__(self):
        return self.name  

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def update_image(cls, id, target, update):
        image_updated = cls.objects.filter(id=id).update(target=update)
        return image_updated

  
    @classmethod
    def get_image_by_id(cls, id):
        image = cls.objects.get(id=id)
        return image

    @classmethod
    def search_by_category(cls, search_term):
        results = cls.objects.filter(category__icontains=search_term)
        return results

    @classmethod
    def filter_by_location(cls, search_term):
        if search_term=='Tanzania':
            return cls.objects.filter(location = 2)
        elif search_term=='Uganda':
            return cls.objects.filter(location = 3) 
        else: 
            return cls.objects.filter(location = 1)                                 