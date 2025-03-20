from django.shortcuts import render
from django.http import HttpResponse
 
def home(request):
    #return HttpResponse("Hello")
    return render(request, 'recipes/pages/home.html', context={
        'name':'Felipe William'
    })

def recipe(request, id): 
    return render(request, 'recipes/pages/recipe-view.html')


# Create your views here.
