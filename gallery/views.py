from django.shortcuts import render, redirect
from .models import location,Category,Image

# Create your views here.

def location_page(request,search_term):
    try:
        if search_term=='Tanzania':
            images = Image.filter_by_location('Tanzania')
            return render(request, 'gallerylab/tz.html',{"images": images})  
        elif search_term=='Uganda':
            images = Image.filter_by_location('Uganda')
            return render(request, 'gallerylab/ug.html',{"images": images}) 
        else: 
            images = Image.filter_by_location('Kenya') 
            return redirect(gallery_page)
    except DoesNotExist:
        raise Http404()
  

def gallery_page(request):
    if 'image' in request.GET and request.GET["image"]:
        filter_location = request.GET.get("image")
        image_results = Image.filter_by_location(filter_location)
        
        return render(request, 'gallerylab/gallery.html',{"images": image_results})

    else:
        image_results = Image.filter_by_location('Kenya')
        return render(request, 'gallerylab/gallery.html',{"images": image_results})

def search_results(request,search_term):

    try:
        if search_term=='Art':
            images = Image.search_by_category('Art')
            return render(request, 'gallerylab/search.html',{"images": images})
        elif search_term=='Nature':
            images = Image.search_by_category('Nature')
            return render(request, 'gallerylab/tz.html',{"images": images})  
        elif search_term=='Culture':
            images = Image.search_by_category('Culture')
            return render(request, 'gallerylab/ug.html',{"images": images}) 
        elif search_term=='Transport':
            images = Image.search_by_category('Transport')
            return render(request, 'gallerylab/ug.html',{"images": images})   
        else: 
            return redirect(gallery_page)

    except DoesNotExist:
        raise Http404()    

