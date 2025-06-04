# asistencia/admin.py

from django.contrib import admin
from .models import Genero, CustomUser # Importa tus modelos
from .models import Servicios
from .models import Estado
from .models import Categorias


# Importa UserAdmin del módulo de autenticación de Django
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Registra Genero (esto ya lo tenías bien)
@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('nombre',) # Muestra el campo 'nombre' en la lista

# Registra CustomUser
@admin.register(CustomUser)
class CustomUserAdmin(BaseUserAdmin):
    # Esto es para mostrar los campos adicionales en la página de edición de un usuario
    # El 'fieldsets' original de UserAdmin incluye username, password, permisos, etc.
    # Aquí le añadimos un nuevo conjunto de campos para tu información adicional.
    fieldsets = BaseUserAdmin.fieldsets + (
        (('Información Adicional', {'fields': ('genero', 'tipo_usuario', 'nacionalidad', 'numDoc', 'telefono', 'fechaNacimiento', 'evidenciaTrabajo', 'experienciaTrabajo', 'hojaVida')}),)
    )

    # Esto es para mostrar los campos adicionales cuando estás creando un NUEVO usuario desde el admin
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        (('Información Adicional', {'fields': ('genero', 'tipo_usuario', 'nacionalidad', 'numDoc', 'telefono', 'fechaNacimiento', 'evidenciaTrabajo', 'experienciaTrabajo', 'hojaVida')}),)
    )

    # Esto es para mostrar los campos en la tabla resumen cuando ves la lista de usuarios
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'tipo_usuario', 'genero') # Añade campos a la vista de lista

    # Puedes añadir campos de búsqueda si quieres (útil para encontrar usuarios)
    search_fields = ('username', 'email', 'first_name', 'last_name', 'numDoc')

    # Puedes añadir filtros (sidebar)
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups', 'tipo_usuario', 'genero')

    # Ordenamiento por defecto en la lista de usuarios
    ordering = ('username',)


@admin.register(Servicios)
class ServiciosAdmin(admin.ModelAdmin):
    list_display = ('NombreServicio', 'idCategorias')  # columnas que quieres mostrar en la lista
    search_fields = ('NombreServicio',)               # para buscar por nombre de servicio
    list_filter = ('idCategorias',) 



@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    list_display = ('Nombre',)
    search_fields = ('Nombre',)

#@admin.register(Pagos)
#class PagosAdmin(admin.ModelAdmin):
#   list_display = ('id', 'Monto', 'estado_pago_texto', 'Fecha', 'idMetodo', 'idestado')
#  search_fields = ('estado_pago_texto',)
# list_filter = ('Fecha', 'idMetodo', 'idestado')

@admin.register(Categorias)
class CategoriasAdmin(admin.ModelAdmin):
    list_display = ('Nombre',)      # Mostrar el nombre de la categoría en la lista
    search_fields = ('Nombre',)     # Permitir buscar por nombre