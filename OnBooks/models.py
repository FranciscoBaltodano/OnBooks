from django.db import models

# Create your models here.
class Idiomas(models.Model):
    IdiomaId = models.AutoField(primary_key = True)
    IdiomaName = models.CharField(max_length = 500)

class GenerosClientes(models.Model):
    GeneroClienteId = models.AutoField(primary_key = True)
    GeneroName = models.CharField(max_length = 500)

class GenerosLiterarios(models.Model):
    GeneroLiterarioId = models.AutoField(primary_key = True)
    GeneroLiterarioName = models.CharField(max_length = 500)

class Ciudades(models.Model):
    CiudadId = models.AutoField(primary_key = True)
    CiudadName = models.CharField(max_length = 500)

class Editoriales(models.Model):
    EditorialId = models.AutoField(primary_key = True)
    EditorialName = models.CharField(max_length = 500)

class Autores(models.Model):
    AutorId = models.AutoField(primary_key = True)
    AutorName = models.CharField(max_length = 500)

class Libros(models.Model):
    LibroId = models.AutoField(primary_key= True)
    LibroName = models.CharField(max_length=200)
    LibroIdioma = models.ForeignKey(Idiomas, null=True, blank=True, on_delete=models.CASCADE)
    LibroGenero = models.ForeignKey(GenerosLiterarios, null=True, blank=True, on_delete=models.CASCADE)
    LibroAutor = models.ForeignKey(Autores, null=True, blank=True, on_delete=models.CASCADE)
    LibroEditorial = models.ForeignKey(Editoriales, null=True, blank=True, on_delete=models.CASCADE)
    