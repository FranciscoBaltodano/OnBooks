from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from OnBooks.models import Idiomas,  GenerosClientes, GenerosLiterarios, Ciudades, Editoriales, Autores, Libros
from OnBooks.serializers import IdiomaSerializer, GeneroClienteSerializer, GeneroLiterarioSerializer, CiudadSerializer, EditorialSerializer, AutorSerializer, LibroSerializer

# Create your views here.

@csrf_exempt 
def idiomaApi(request, id=0):
    if request.method=='GET':
        idiomas = Idiomas.objects.all()
        idioma_serializer =  IdiomaSerializer(idiomas, many = True)
        return JsonResponse(idioma_serializer.data, safe=False)
    elif request.method == 'POST':
        idioma_data = JSONParser().parse(request)
        idioma_serializer = IdiomaSerializer(data = idioma_data)
        if idioma_serializer.is_valid():
            idioma_serializer.save()
            return JsonResponse('Añadido Exitosamente!!!',safe=False)
        return JsonResponse("Fallo al intentar agregar", safe=False)
    elif request.method=='PUT':
        idioma_data = JSONParser().parse(request)
        idioma = Idiomas.objects.get(IdiomaId=idioma_data['IdiomaId'])
        idioma_serializer = IdiomaSerializer(idioma, data=idioma_data)
        if idioma_serializer.is_valid():
            idioma_serializer.save()
            return JsonResponse('Actualizado Exitosamente!!!!',safe=False)
        return JsonResponse("Fallo al Actualizar")
    elif request.method=='DELETE':
        idioma = Idiomas.objects.get(IdiomaId=id)
        idioma.delete()
        return JsonResponse('Eliminado Exitosamente', safe=False)

@csrf_exempt
def generoClienteApi(request, id=0):
    if request.method=='GET':
        generosCliente = GenerosClientes.objects.all()
        generoCliente_serializer =  GeneroClienteSerializer(generosCliente, many = True)
        return JsonResponse(generoCliente_serializer.data, safe=False)
    elif request.method == 'POST':
        generoCliente_data = JSONParser().parse(request)
        generoCliente_serializer = GeneroClienteSerializer(data = generoCliente_data)
        if generoCliente_serializer.is_valid():
            generoCliente_serializer.save()
            return JsonResponse('Añadido Exitosamente!!!',safe=False)
        return JsonResponse("Fallo al intentar agregar", safe=False)
    elif request.method=='PUT':
        generoCliente_data = JSONParser().parse(request)
        generoCliente = GenerosClientes.objects.get(GeneroClienteId=generoCliente_data['GeneroClienteId'])
        generoCliente_serializer = GeneroClienteSerializer(generoCliente, data=generoCliente_data)
        if generoCliente_serializer.is_valid():
            generoCliente_serializer.save()
            return JsonResponse('Actualizado Exitosamente!!!!',safe=False)
        return JsonResponse("Fallo al Actualizar")
    elif request.method=='DELETE':
        generoCliente = GenerosClientes.objects.get(GeneroClienteId=id)
        generoCliente.delete()
        return JsonResponse('Eliminado Exitosamente', safe=False)

@csrf_exempt 
def generoLiterarioApi(request, id=0):
    if request.method=='GET':
        generosLiterarios = GenerosLiterarios.objects.all()
        generoLiterario_serializer =  GeneroLiterarioSerializer(generosLiterarios, many = True)
        return JsonResponse(generoLiterario_serializer.data, safe=False)
    elif request.method == 'POST':
        generoLiterario_data = JSONParser().parse(request)
        generoLiterario_serializer = GeneroLiterarioSerializer(data = generoLiterario_data)
        if generoLiterario_serializer.is_valid():
            generoLiterario_serializer.save()
            return JsonResponse('Añadido Exitosamente!!!',safe=False)
        return JsonResponse("Fallo al intentar agregar", safe=False)
    elif request.method=='PUT':
        generoLiterario_data = JSONParser().parse(request)
        generoLiterario = GenerosLiterarios.objects.get(GeneroLiterarioId=generoLiterario_data['GeneroLiterarioId'])
        generoLiterario_serializer = GeneroLiterarioSerializer(generoLiterario, data=generoLiterario_data)
        if generoLiterario_serializer.is_valid():
            generoLiterario_serializer.save()
            return JsonResponse('Actualizado Exitosamente!!!!',safe=False)
        return JsonResponse("Fallo al Actualizar")
    elif request.method=='DELETE':
        generoLiterario = GenerosLiterarios.objects.get(GeneroLiterarioId=id)
        generoLiterario.delete()
        return JsonResponse('Eliminado Exitosamente', safe=False)

# @csrf_exempt #LITERARIO
# def generoLiterarioApi(request, id=0):
#     if request.method=='GET':
#         generosLiterario = GenerosLiterarios.objects.all()
#         generoLiterario_serializer =  GeneroLiterarioSerializer(generosLiterario, many = True)
#         return JsonResponse(generoLiterario_serializer.data, safe=False)
#     elif request.method == 'POST':
#         generoLiterario_data = JSONParser().parse(request)
#         generoLiterario_serializer = GeneroLiterarioSerializer(data = generoLiterario_data)
#         if generoLiterario_serializer.is_valid():
#             generoLiterario_serializer.save()
#             return JsonResponse('Añadido Exitosamente!!!',safe=False)
#         return JsonResponse("Fallo al intentar agregar", safe=False)
#     elif request.method=='PUT':
#         generoLiterario_data = JSONParser().parse(request)
#         generoLiterario = GenerosLiterarios.objects.get(GeneroLiterarioId=generoLiterario_data['GeneroLiterarioId'])
#         generoLiterario_serializer = GeneroLiterarioSerializer(generoLiterario, data=generoLiterario_data)
#         if generoLiterario_serializer.is_valid():
#             generoLiterario_serializer.save()
#             return JsonResponse('Actualizado Exitosamente!!!!',safe=False)
#         return JsonResponse("Fallo al Actualizar")
#     elif request.method=='DELETE':
#         generoLiterario = GenerosLiterarios.objects.get(GeneroLiterarioId=id)
#         generoLiterario.delete()
#         return JsonResponse('Eliminado Exitosamente', safe=False)

@csrf_exempt
def ciudadApi(request, id=0):
    if request.method=='GET':
        ciudades = Ciudades.objects.all()
        ciudad_serializer =  CiudadSerializer(ciudades, many = True)
        return JsonResponse(ciudad_serializer.data, safe=False)
    elif request.method == 'POST':
        ciudad_data = JSONParser().parse(request)
        ciudad_serializer = CiudadSerializer(data = ciudad_data)
        if ciudad_serializer.is_valid():
            ciudad_serializer.save()
            return JsonResponse('Añadido Exitosamente!!!',safe=False)
        return JsonResponse("Fallo al intentar agregar", safe=False)
    elif request.method=='PUT':
        ciudad_data = JSONParser().parse(request)
        ciudad = Ciudades.objects.get(CiudadId=ciudad_data['CiudadId'])
        ciudad_serializer = CiudadSerializer(ciudad, data=ciudad_data)
        if ciudad_serializer.is_valid():
            ciudad_serializer.save()
            return JsonResponse('Actualizado Exitosamente!!!!',safe=False)
        return JsonResponse("Fallo al Actualizar")
    elif request.method=='DELETE':
        ciudad = Ciudades.objects.get(CiudadId=id)
        ciudad.delete()
        return JsonResponse('Eliminado Exitosamente', safe=False)


@csrf_exempt
def editorialApi(request, id=0):
    if request.method=='GET':
        editoriales = Editoriales.objects.all()
        editorial_serializer =  EditorialSerializer(editoriales, many = True)
        return JsonResponse(editorial_serializer.data, safe=False)
    elif request.method == 'POST':
        editorial_data = JSONParser().parse(request)
        editorial_serializer = EditorialSerializer(data = editorial_data)
        if editorial_serializer.is_valid():
            editorial_serializer.save()
            return JsonResponse('Añadido Exitosamente!!!',safe=False)
        return JsonResponse("Fallo al intentar agregar", safe=False)
    elif request.method=='PUT':
        editorial_data = JSONParser().parse(request)
        editorial = Editoriales.objects.get(EditorialId=editorial_data['EditorialId'])
        editorial_serializer = EditorialSerializer(editorial, data=editorial_data)
        if editorial_serializer.is_valid():
            editorial_serializer.save()
            return JsonResponse('Actualizado Exitosamente!!!!',safe=False)
        return JsonResponse("Fallo al Actualizar")
    elif request.method=='DELETE':
        editorial = Editoriales.objects.get(EditorialId=id)
        editorial.delete()
        return JsonResponse('Eliminado Exitosamente', safe=False)


@csrf_exempt 
def autorApi(request, id=0):
    if request.method=='GET':
        autores = Autores.objects.all()
        autor_serializer =  AutorSerializer(autores, many = True)
        return JsonResponse(autor_serializer.data, safe=False)
    elif request.method == 'POST':
        autor_data = JSONParser().parse(request)
        autor_serializer = AutorSerializer(data = autor_data)
        if autor_serializer.is_valid():
            autor_serializer.save()
            return JsonResponse('Añadido Exitosamente!!!',safe=False)
        return JsonResponse("Fallo al intentar agregar", safe=False)
    elif request.method=='PUT':
        autor_data = JSONParser().parse(request)
        autor = Autores.objects.get(AutorId=autor_data['AutorId'])
        autor_serializer = AutorSerializer(autor, data=autor_data)
        if autor_serializer.is_valid():
            autor_serializer.save()
            return JsonResponse('Actualizado Exitosamente!!!!',safe=False)
        return JsonResponse("Fallo al Actualizar")
    elif request.method=='DELETE':
        autor = Autores.objects.get(AutorId=id)
        autor.delete()
        return JsonResponse('Eliminado Exitosamente', safe=False)




@csrf_exempt 
def libroApi(request, id=0):
    if request.method=='GET':
        libros = Libros.objects.all()
        libro_serializer =  LibroSerializer(libros, many = True)
        return JsonResponse(libro_serializer.data, safe=False)
    elif request.method == 'POST':
        libro_data = JSONParser().parse(request)
        libro_serializer = LibroSerializer(data = libro_data)
        if libro_serializer.is_valid():
            libro_serializer.save()
            return JsonResponse('Añadido Exitosamente!!!',safe=False)
        return JsonResponse("Fallo al intentar agregar", safe=False)
    elif request.method=='PUT':
        libro_data = JSONParser().parse(request)
        libro = Libros.objects.get(LibroId=libro_data['LibroId'])
        libro_serializer = LibroSerializer(libro, data=libro_data)
        if libro_serializer.is_valid():
            libro_serializer.save()
            return JsonResponse('Actualizado Exitosamente!!!!',safe=False)
        return JsonResponse("Fallo al Actualizar")
    elif request.method=='DELETE':
        libro = Libros.objects.get(LibroId=id)
        libro.delete()
        return JsonResponse('Eliminado Exitosamente', safe=False)
