from rest_framework import serializers
from OnBooks.models import Idiomas,  GenerosClientes, GenerosLiterarios, Ciudades, Editoriales, Autores, Libros

class IdiomaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idiomas 
        fields = ('IdiomaId', 'IdiomaName')

class GeneroClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenerosClientes 
        fields = ('GeneroClienteId', 'GeneroName')

class GeneroLiterarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenerosLiterarios
        fields = ('GeneroLiterarioId', 'GeneroLiterarioName')

class CiudadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudades 
        fields = ('CiudadId', 'CiudadName')

class EditorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editoriales
        fields = ('EditorialId', 'EditorialName')

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autores 
        fields = ('AutorId', 'AutorName', 'AutorDate')

class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libros 
        fields = ('LibroId', 'LibroName', 'LibroIdioma', 'LibroGenero', 'LibroAutor', 'LibroEditorial')



