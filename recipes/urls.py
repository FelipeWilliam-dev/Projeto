from django.urls import path
#from recipes.views import home, contato #inclui todos as urls
from . import views # Nesse caso, é preciso adicionar "views." na frente da importação
#from recipes.views import home, contato, sobre

urlpatterns = [
    path('', views.home),
    path('recipes/<int:id>/', views.recipe),
]
