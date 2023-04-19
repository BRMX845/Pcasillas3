
from rest_framework import serializers
from .models import Usuarios, Casilla, AlquilerCasillas,Departamento
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group
class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'
        
class UsuariosSerializer(serializers.ModelSerializer):
    def validate_password(self, value):
        return make_password(value)
    class Meta:
        model = Usuarios
        fields = ['id','username','password','email','celular','ci','departamento','first_name','last_name']
        #depth=1
    def create(self, validated_data):
        validated_data['is_superuser'] = False
        validated_data['is_staff'] = False
        validated_data['is_active'] = True
        user = Usuarios.objects.create_user(**validated_data)
        group = Group.objects.get(name='cliente') # Cambia el nombre del grupo aquí
        user.groups.add(group)
        return user
class CasillaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Casilla
        fields = '__all__'
        #depth=1 
        #para mostrar la llaveforanea

class AlquilerCasillasSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlquilerCasillas
        fields = '__all__'
        #depth=1

