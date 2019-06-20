from django.urls import path
from .views import saludar,otraP, guardarMesero

urlpatterns = [
    path('', saludar, name='principal'),
    path('saving/', guardarMesero, name='guardarMese'),
    path('otrapaginasi/', otraP, name='otrapage'),

]