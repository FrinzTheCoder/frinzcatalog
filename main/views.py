from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from main.models import *

def homepage(request):
    return render(request, 'home/main.html')

def catalog(request):
    return render(request, 'catalog/catalog.html')

def catalog_handler(request, type):
    context = {
        'type':type
    }
    if type == 'Monera':
        context['description'] = 'Monera is historically a biological kingdom that is made up of prokaryotes. As such, it is composed of single-celled organisms that lack a nucleus.'
        return render(request, 'catalog/catalog_page.html', context)
    elif type == 'Protist':
        context['description'] = 'A protist is any eukaryotic organism that is not an animal, plant, or fungus. Protists do not form a natural group, or clade, but an artificial grouping of several independent clades that evolved from the last eukaryotic common ancestor.'
        return render(request, 'catalog/catalog_page.html', context)
    elif type == 'Fungi':
        context['description'] = 'A fungus is any member of the group of eukaryotic organisms that includes microorganisms such as yeasts and molds, as well as the more familiar mushrooms.'
        return render(request, 'catalog/catalog_page.html', context)
    elif type == 'Plantae':
        context['description'] = 'Plants are the eukaryotes that form the kingdom Plantae. They are predominantly photosynthetic, means that they obtain their energy from sunlight using the green pigment chlorophyll.'
        return render(request, 'catalog/catalog_page.html', context)
    elif type == 'Animalia':
        context['description'] = 'Animals are multicellular, eukaryotic organisms in the biological kingdom Animalia. With few exceptions, animals consume organic material, breathe oxygen, have myocytes and are able to move, can reproduce sexually, and grow from a hollow sphere of cells, the blastula, during embryonic development.'
        return render(request, 'catalog/catalog_page.html', context)
    else:
        context['description'] = 'Just random stuffs that are inanimate, unidentified, or unclassified.'
        return render(request, 'catalog/catalog_page.html', context)

def catalog_monera(request):
    return catalog_handler(request, 'Monera')

def catalog_protist(request):
    return catalog_handler(request, 'Protist')

def catalog_fungi(request):
    return catalog_handler(request, 'Fungi')

def catalog_plantae(request):
    return catalog_handler(request, 'Plantae')

def catalog_animalia(request):
    return catalog_handler(request, 'Animalia')

def catalog_random(request):
    return catalog_handler(request, 'Random')

def catalog_find(request, content_type, name):
    if request.method == "GET":
        category = type_mapper(content_type)
        contents = Content.objects.filter(name__icontains=name, category=category.name)
        return HttpResponse(serializers.serialize("json", contents), content_type="application/json")
    return HttpResponse("Invalid method", status=405)

def catalog_getall_by_type(request, content_type):
    if request.method == "GET":
        category = type_mapper(content_type)
        contents = Content.objects.filter(category=category.name)
        return HttpResponse(serializers.serialize("json", contents), content_type="application/json")
    return HttpResponse("Invalid method", status=405)

def type_mapper(content_type):
    if content_type=='Monera':
        return Category.MONERA
    elif content_type=='Protist':
        return Category.PROTIST
    elif content_type=='Fungi':
        return Category.FUNGI
    elif content_type=='Plantae':
        return Category.PLANTAE
    elif content_type=='Animalia':
        return Category.ANIMALIA
    elif content_type=='Random':
        return Category.RANDOM
    else:
        pass