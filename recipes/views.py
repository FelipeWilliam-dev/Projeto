from django.shortcuts import render
from django.http import HttpResponse
 
def home(request):
    #return HttpResponse("Hello")
    return render(request, 'recipes/pages/home.html', context={
        'name':'Felipe William'
    })

def contato(request): 
    return HttpResponse("Nicolas Passivo")


# Create your views here.
