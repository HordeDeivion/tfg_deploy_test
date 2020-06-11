from django.db import models
from django.utils.timezone import now as timezone_now

# Create your models here.

class AREA_PROFESIONAL(models.Model):

    nombre_area = models.CharField(
        max_length = 100,
        primary_key = True
    )

class PROFESIONAL(models.Model):

    identificador_medico = models.IntegerField(
        null= False,
        default = -1,
        primary_key= True
    )
    nombre = models.CharField(
        null = False,
        default= '',
        max_length= 150
    )

    apellido1 = models.CharField(
        null = False,
        default='',
        max_length= 150
    )

    apellido2 = models.CharField(
        blank=True,
        default = '',
        max_length= 150
    )
    edad = models.IntegerField(
        null = False
    )

    area = models.ForeignKey(
       to = AREA_PROFESIONAL,
       null = False,
       on_delete = models.CASCADE
    )
    
    def __str__(self):
        return "Soy el profesional" + self.pk


class RECURSO(models.Model):
    
    
    nombre_recurso = models.CharField(
        null = False,
        max_length= 50
    )
    tipo = models.CharField(
        null = False,
        max_length= 50
    )

    def __str__(self):
        return "Soy el recurso" + self.pk

class ACTIVIDAD(models.Model):
    nombre_actividad = models.CharField(
        null = False,
        max_length = 50
    )
    tipo = models.ForeignKey(
        to=RECURSO,
        null=False,
        on_delete=models.CASCADE,
        verbose_name='tipo de recuerso profesional asociado a una actividad'
    )
    def __str(self):
        return "Soy la actividad" + self.pk
    
class PROCEDIMIENTOS(models.Model):
    nombre_procedimiento = models.CharField(
        null = False,
        max_length = 100
    )
class PACIENTE(models.Model):
    nombre = models.CharField(
        null=False,
        default='',
        max_length = 150
    )
    apellido1 = models.CharField(
        null=False,
        default = '',
        max_length = 150
    )
    apellido2 = models.CharField(
        blank=True,
        default= '',
        max_length=150
    )

    edad = models.IntegerField(
        null = False
    )
    fecha_inclusion = models.DateField(
        default=timezone_now
    )
    diagnostico = models.CharField(
        null = False,
        max_length= 150
    )
    procedimiento_paciente = models.ForeignKey(
        to = PROCEDIMIENTOS,
        null=False,
        on_delete=models.CASCADE,
        verbose_name='tipo de procedimiento asociado a un paciente'
    )
    actividad_paciente = models.ForeignKey(
        to = ACTIVIDAD,
        null=False,
        on_delete=models.CASCADE,
        verbose_name='Actividad asociada a un paciente'
    )
    profesional_paciente = models.ForeignKey(
        to = PROFESIONAL,
        null=False,
        on_delete=models.CASCADE,
        verbose_name='Profesional asociado a un paciente'
    )

    def __str__(self):
        return "Soy el paciente" + self.pk
