#from django.shortcuts import render

# Create your views here.
#importo api para la vista
from rest_framework.views import APIView
from rest_framework.response import Response
#importar serializadores y modelos
from .models import Usuarios, Casilla, AlquilerCasillas,Departamento
from .serializers import UsuariosSerializer, CasillaSerializer, AlquilerCasillasSerializer ,DepartamentoSerializer
#para la autenticacion 
from rest_framework.permissions import IsAuthenticated,DjangoModelPermissions

from django.shortcuts import get_object_or_404

from rest_framework import status
class DepartamentoList(APIView):
    queryset=Departamento.objects.all()
    serializer_class= DepartamentoSerializer
    permission_classes = (IsAuthenticated,DjangoModelPermissions)
    def get(self, request, pk=None):
        if pk is not None:
            departamento = get_object_or_404(Departamento, pk=pk)
            serializer = DepartamentoSerializer(departamento)
            return Response(serializer.data)
        else:
            departamentos = Departamento.objects.all()
            serializer = DepartamentoSerializer(departamentos, many=True)
            return Response(serializer.data)
    def post(self, request):
        serializer = DepartamentoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, pk):
        departamento = get_object_or_404(Departamento, pk=pk)
        serializer = DepartamentoSerializer(departamento, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        departamento = get_object_or_404(Departamento, pk=pk)
        departamento.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class UsuariosList(APIView):
    queryset=Usuarios.objects.all()
    serializer_class= UsuariosSerializer
    permission_classes = (IsAuthenticated,DjangoModelPermissions)
    def get(self, request, pk=None):
        if pk is not None:
            usuario = get_object_or_404(Usuarios, pk=pk)
            serializer = UsuariosSerializer(usuario)
            return Response(serializer.data)
        else:
            #hago que se flite por la session iniciada
            usuarios = Usuarios.objects.filter(id=request.user.id)
            serializer = UsuariosSerializer(usuarios, many=True)
            return Response(serializer.data)
    def post(self, request):
        serializer = UsuariosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, pk):
        usuario = get_object_or_404(Usuarios, pk=pk)
        serializer = UsuariosSerializer(usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        usuario = get_object_or_404(Usuarios, pk=pk)
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class CasillaList(APIView):
    queryset=Casilla.objects.all()
    serializer_class= CasillaSerializer
    permission_classes = (IsAuthenticated,DjangoModelPermissions)
    def get(self, request, pk=None):
        if pk is not None:
            casilla = get_object_or_404(Casilla, pk=pk)
            serializer = CasillaSerializer(casilla)
            return Response(serializer.data)
        else:
            casillas = Casilla.objects.all()
            serializer = CasillaSerializer(casillas, many=True)
            return Response(serializer.data)
    def post(self, request):
        serializer = CasillaSerializer(data=request.data)
        #condicional de validacion de datos para guardarlos en la base de datos
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, pk):
        casilla = get_object_or_404(Casilla, pk=pk)
        serializer = CasillaSerializer(casilla, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        casilla = get_object_or_404(Casilla, pk=pk)
        casilla.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class AlquilerCasillasList(APIView):
    #solitica el token de inicio de session
    queryset=AlquilerCasillas.objects.all()
    serializer_class= AlquilerCasillasSerializer
    permission_classes = (IsAuthenticated,DjangoModelPermissions)
    def get(self, request, pk=None):
        if pk is not None:
            alqcasilla = get_object_or_404(AlquilerCasillas, pk=pk)
            serializer = AlquilerCasillasSerializer(alqcasilla)
            return Response(serializer.data)
        else:
            alqcasillas = AlquilerCasillas.objects.all()
            serializer = AlquilerCasillasSerializer(alqcasillas, many=True)
            return Response(serializer.data)
    def post(self, request):
        serializer = AlquilerCasillasSerializer(data=request.data)
        #condicional de validacion de datos para guardarlos en la base de datos
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, pk):
        alqcasillas = get_object_or_404(AlquilerCasillas, pk=pk)
        serializer = AlquilerCasillasSerializer(alqcasillas, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        alqcasillas = get_object_or_404(AlquilerCasillas, pk=pk)
        alqcasillas.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)