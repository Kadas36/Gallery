from django.shortcuts import render
from .models import location,Category,Image

# Create your views here.

def location_page(request):
    if 'image' in request.GET and request.GET["image"]:
        filter_location = request.GET.get("image")
        image_results = Image.filter_by_location(filter_location)
        
        return render(request, 'gallerylab/base.html',{"images": image_results})

    else:
        image_results = Image.filter_by_location('Kenya')
        return render(request, 'gallerylab/base.html',{"images": image_results})

def gallery_page(request):
    if 'image' in request.GET and request.GET["image"]:
        filter_location = request.GET.get("image")
        image_results = Image.filter_by_location(filter_location)
        
        return render(request, 'gallerylab/gallery.html',{"images": image_results})

    else:
        image_results = Image.filter_by_location('Kenya')
        return render(request, 'gallerylab/gallery.html',{"images": image_results})

  