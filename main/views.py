from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from main.models import *
from django.db import transaction

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

def content_display(request, id):
    if request.method == "GET":
        content = Content.objects.get(id=id)
        context = {'content':content}
        return render(request, 'catalog/content_page.html', context)
    return HttpResponse("Invalid method", status=405)

def get_like(request, id):
    if request.method == "GET":
        client_ip = request.META.get('HTTP_X_FORWARDED_FOR', None) or \
        request.META.get('HTTP_X_REAL_IP', None) or \
        request.META.get('REMOTE_ADDR', None)
        content = Content.objects.get(id=id)

        number_of_likes = content.likes.filter(is_like=True).count()
        
        if client_ip != None:
            filtered_like = content.likes.filter(ip_address=client_ip)
            if len(filtered_like)!=0:
                is_like = filtered_like[0].is_like
            else:
                is_like = False
        else:
            is_like = False
        payload = {'is_like':is_like, 'number_of_likes':number_of_likes}
        return JsonResponse(payload, status=200)
    return HttpResponse("Invalid method", status=405)

@transaction.atomic
@csrf_exempt
def content_like(request):
    if request.method == "POST":
        # getting the user's IP Address
        client_ip = request.META.get('HTTP_X_FORWARDED_FOR', None) or \
        request.META.get('HTTP_X_REAL_IP', None) or \
        request.META.get('REMOTE_ADDR', None)

        # getting the content id to be liked
        content_id = int(request.body)

        if client_ip == None: # failed to get user's IP Address
            return HttpResponse("Failed to get user's IP Address", status=400)

        # get the like from an ip address
        content = Content.objects.get(id=content_id)
        like = content.likes.filter(ip_address=client_ip)

        if len(like) == 0:
            new_like = Like.objects.create(ip_address=client_ip, is_like=True)
            content.likes.add(new_like)
            return HttpResponse("Success", status=200)
        else:
            like_obj = like[0]
            if like_obj.is_like == True:
                like_obj.is_like = False
            else:
                like_obj.is_like = True
            like_obj.save()
            return HttpResponse("Sucess", status=200)
    return HttpResponse("Invalid method", status=405)