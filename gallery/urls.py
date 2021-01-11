from django.urls import path,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.urls.resolvers import URLPattern
from . import views
import gallery

urlpatterns=[
    path('', views.gallery_page, name='gallery_page'),
    path('<str:search_term>/',views.location_page,name ='locationPage'),
    re_path(r'^search_term/', views.search_results, name='search_results'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
