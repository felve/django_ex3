from django.contrib import admin

from .models import (
 	Region,
	Ciudad,
	Vivienda,
	Razaprodominante,
	Interesados,
	Mascotas,
	Estados
)


admin.site.register(Region)
admin.site.register(Ciudad)
admin.site.register(Vivienda)
admin.site.register(Razaprodominante)
admin.site.register(Mascotas)
admin.site.register(Interesados)
admin.site.register(Estados)

