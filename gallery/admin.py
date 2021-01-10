from django.contrib import admin
from .models import location,Category,Image

# Register your models here.

class GalleryAdmin(admin.ModelAdmin):
    filter_horizontal =('category',)

admin.site.register(location)
admin.site.register(Category)
admin.site.register(Image)
