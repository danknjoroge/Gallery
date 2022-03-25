from django.shortcuts import render
from django.http import HttpResponse
from .models import Image

# Create your views here.
def index(request):
    image = Image.objects.all()
    return render(request, 'index.html', {'image': image})

def one_image(request):
    return render(request, 'one_image.html')

# def search(request):
#     if 'image' in request.GET and request.GET["image"]:
#         name = request.GET.get('image')
#         searchname= Image.search_by_name(name)
#         message = f"{name}"

#         return render(request, 'search.html',{"message":message, "image":searchname})

#     else:
#         message = "There are no results associated with the search term"
#         return render(request, 'search.html', {'message':message})


def search(request):
    if 'image' in request.GET and request.GET["image"]:
        category = request.GET.get('image')
        searchname= Image.search_by_category(category)
        message = f"{category}"

        return render(request, 'search.html',{"message":message, "image":searchname})

    else:
        message = "There are no results associated with the search term"
        return render(request, 'search.html', {'message':message})




