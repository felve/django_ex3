from .models import Interesados, Mascotas
from rest_framework import serializers

class MascotaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Mascotas
		fields = ('nombre','razap','descripcion','estados','image')
		
class interesasosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interesados
        fields = ('rut','nombrecompleto','correo','telefono','region','ciudad','vivienda','fecha_nacimiento')
