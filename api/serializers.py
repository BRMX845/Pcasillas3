
from rest_framework import serializers
from .models import Usuarios, Casilla, AlquilerCasillas,Departamento
from django.contrib.auth.hashers import make_password
class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'
        
class UsuariosSerializer(serializers.ModelSerializer):
    def validate_password(self, value):
        return make_password(value)
    class Meta:
        model = Usuarios
        fields = ['id','username','password','email','celular','ci','departamento','is_superuser','first_name','last_name','is_staff','is_active']

class CasillaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Casilla
        fields = '__all__'
        depth=1 #para mostrar la llaveforanea

class AlquilerCasillasSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlquilerCasillas
        fields = '__all__'

