from django.shortcuts import render
from django.http import HttpResponse
 
def home(request):
    #return HttpResponse("Hello")
    return render(request, 'home.html')

def contato(request):
    return HttpResponse("Nicolas Passivo")

def sobre(request):
    return HttpResponse("Hey Brow")



# Create your views here.
