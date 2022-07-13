from pickle import FALSE
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Suscripcion
from django.contrib.auth.models import User
from .serializers import SuscripcionSerializer

@csrf_exempt
@api_view(['POST'])
def obtener_suscripcion(request):
    """
    LISTA SUSCRIPCION 
    """
    if request.method == 'POST':
        data = JSONParser().parse(request)
        id_usuario = data['id_usuario']

        try:
            user = User.objects.get(username=id_usuario)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
       
        try:
            suscripcion = Suscripcion.objects.get(usuario=user)
        except Suscripcion.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)       
       
        serializer = SuscripcionSerializer(suscripcion)
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['PUT'])
def activar_suscripcion(request):
    """
    ACTIVAR SUSCRIPCIÓN
    """
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        id_usuario = data['id_usuario']

        try:
            user = User.objects.get(username=id_usuario)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        suscripcion = Suscripcion.objects.get(usuario=user)
        suscripcion.vigente = True
        suscripcion.save()

        serializer = SuscripcionSerializer(suscripcion)
        return Response(serializer.data)

@csrf_exempt
@api_view(['PUT'])
def eliminar_suscripcion(request):
    """
    ELIMINAR SUSCRIPCIÓN
    """
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        id_usuario = data['id_usuario']

        try:
            user = User.objects.get(username=id_usuario)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        suscripcion = Suscripcion.objects.get(usuario=user)
        suscripcion.vigente = False
        suscripcion.save()

        serializer = SuscripcionSerializer(suscripcion)
        return Response(serializer.data)

    
