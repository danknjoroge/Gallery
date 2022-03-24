from django.shortcuts import render
from django.http import HttpResponse
from .models import Image

# Create your views here.
def index(request):
    image = Image.objects.all()
    return render(request, 'index.html', {'image': image})

def one_image(request):
    return render(request, 'one_image.html')