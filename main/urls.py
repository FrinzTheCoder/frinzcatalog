from django.urls import path
from main.views import * 

app_name = 'main'

urlpatterns = [
    path('', homepage, name='homepage'),
    path('catalog', catalog, name='catalog')
]