from django.contrib import admin

from .models import Registro, Medicamento, Usuario, InsumoMedico


# Register your models here.

admin.site.register(Registro)
admin.site.register(Medicamento)
admin.site.register(Usuario)
admin.site.register(InsumoMedico)
