from django.shortcuts import render

def homepage(request):
    return render(request, 'home/main.html')

def catalog(request):
    return render(request, 'catalog/catalog.html')