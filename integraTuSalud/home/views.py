from django.shortcuts import render
from django.http import HttpResponse
from .models import Articulo

def index(request):
    #return HttpResponse("hello world.")
    #context = {User.objects.all}
    return render(request, 'wizard/index.html')

def articulo(request):
    latest_article_list = Articulo.objects.order_by('-fecha')[:5]
    output = ', '.join([p.titulo for p in latest_article_list])
    return HttpResponse(output)

# Create your views here.
