from django.urls import path, re_path
from django.urls.resolvers import URLPattern
from . import views
import gallery

urlpatterns=[
    path('', views.gallery_page, name='gallery_page'),
]
