from django.urls import re_path
from OnBooks import views

urlpatterns = [
    re_path(r'^idioma$', views.idiomaApi),
    re_path(r'^idioma/([0-9]+)$', views.idiomaApi),
    
    re_path(r'^generoCliente$', views.generoClienteApi),
    re_path(r'^generoCliente/([0-9]+)$', views.generoClienteApi),
    
    re_path(r'^generoLiterario$', views.generoLiterarioApi),
    re_path(r'^generoLiterario/([0-9]+)$', views.generoLiterarioApi),
    
    re_path(r'^ciudad$', views.ciudadApi),
    re_path(r'^ciudad/([0-9]+)$', views.ciudadApi),
    
    re_path(r'^editorial$', views.editorialApi),
    re_path(r'^editorial/([0-9]+)$', views.editorialApi),
    
    re_path(r'^autor$', views.autorApi),
    re_path(r'^autor/([0-9]+)$', views.autorApi),
    
    re_path(r'^libro$', views.libroApi),
    re_path(r'^libro/([0-9]+)$', views.libroApi),
]