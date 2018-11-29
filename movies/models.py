from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator

User = get_user_model()


class Region(models.Model):
    """Modelo de Estudio de cine."""

    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name		

class Ciudad(models.Model):
    """Modelo de Estudio de cine."""

    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name		

class Vivienda(models.Model):
    """Modelo de Estudio de cine."""

    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name

class Razaprodominante(models.Model):
    """Modelo de Estudio de cine."""

    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name		

class Estados(models.Model):
    """Modelo de Estudio de cine."""

    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name
		
	
		
	
class Interesados(models.Model):
 rut = models.CharField('Rut', max_length=12)
 nombrecompleto = models.CharField('Nombre Completo', max_length=100)
 correo = models.EmailField()
 telefono = models.IntegerField()
 region = models.ManyToManyField('Region')
 ciudad = models.ManyToManyField('Ciudad')
 vivienda = models.ManyToManyField('Vivienda')
 fecha_nacimiento = models.DateField('Fecha de nacimiento')
 password = models.CharField(max_length=50)
 
 def __str__(self):
        return self.nombrecompleto
		
		

class Mascotas(models.Model):
 nombre = models.CharField('Nombre mascota', max_length=20)
 razap = models.ManyToManyField('Razaprodominante')
 descripcion = models.CharField(max_length=30)
 estados= models.ManyToManyField('Estados')
 image = models.ImageField(upload_to='albums/images/')
 
 def __str__(self):
        return self.nombre
		


	
