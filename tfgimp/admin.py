from django.contrib import admin
from .models import PACIENTE,PROCEDIMIENTOS,PROFESIONAL,ACTIVIDAD, RECURSO, AREA_PROFESIONAL
# Register your models here.


admin.site.register(PACIENTE)
admin.site.register(AREA_PROFESIONAL)
admin.site.register(PROCEDIMIENTOS)
admin.site.register(PROFESIONAL)
admin.site.register(ACTIVIDAD)
admin.site.register(RECURSO)