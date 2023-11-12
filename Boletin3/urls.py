from django.urls import path
from Boletin3 import views

urlpatterns = [
    
    path('', views.subir_imagen, name='subir_imagen'),
    path('galeria/', views.galeria, name='galeria'),
    

]
