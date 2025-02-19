from django.urls import path
from recipes.views import home, contato, sobre #inclui todos as urls
#from recipes.views import home, contato, sobre

urlpatterns = [
    path('', home),
    path('contato/', contato),
    path('sobre/', sobre),
]
