#from django.shortcuts import render

# Create your views here.
#importo api para la vista
from rest_framework.views import APIView
from rest_framework.response import Response
#importar serializadores y modelos
from .models import Usuarios, Casilla, AlquilerCasillas,Departamento
from .serializers import UsuariosSerializer, CasillaSerializer, AlquilerCasillasSerializer ,DepartamentoSerializer
#
from rest_framework.permissions import AllowAny
class DepartamentoList(APIView):
    #peticion get de la tabla Departamento
    def get(self, request):
        departamento = Departamento.objects.all()
        serializer = DepartamentoSerializer(departamento, many=True)
        return Response(serializer.data)
    #peticion post para la insercion de datos 
    def post(self, request):
        serializer = DepartamentoSerializer(data=request.data)
        #condicional de validacion de datos para guardarlos en la base de datos
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class UsuariosList(APIView):
    def get(self, request):
        usuario = Usuarios.objects.all()
        serializer = UsuariosSerializer(usuario, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = UsuariosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CasillaList(APIView):
    def get(self, request):
        casillas = Casilla.objects.all()
        serializer = CasillaSerializer(casillas, many=True, context={'request': request})
        return Response(serializer.data)
    def post(self, request):
        serializer = CasillaSerializer(data=request.data)
        #condicional de validacion de datos para guardarlos en la base de datos
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class AlquilerCasillasList(APIView):
    def get(self, request):
        alquileres = AlquilerCasillas.objects.all()
        serializer = AlquilerCasillasSerializer(alquileres, many=True)
        return Response(serializer.data)