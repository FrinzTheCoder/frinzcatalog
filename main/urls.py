from django.urls import path
from main.views import * 

app_name = 'main'

urlpatterns = [
    path('', homepage, name='homepage'),
    path('catalog', catalog, name='catalog'),
    path('catalog/monera', catalog_monera, name='catalog-monera'),
    path('catalog/protist', catalog_protist, name='catalog-protist'),
    path('catalog/fungi', catalog_fungi, name='catalog-fungi'),
    path('catalog/plantae', catalog_plantae, name='catalog-plantae'),
    path('catalog/animalia', catalog_animalia, name='catalog-animalia'),
    path('catalog/random', catalog_random, name='catalog-random'),
    path('catalog/getallbytype/<str:content_type>', catalog_getall_by_type, name='catalog-getall-by-type'),
    path('catalog/<str:content_type>/<str:name>', catalog_find, name='catalog-find'),
    path('content/<int:id>', content_display, name='content-display'),
    path('like/', content_like, name='content-like'),
    path('get_like/<int:id>', get_like, name='get-like'),
]