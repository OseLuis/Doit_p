# asistencia/urls.py

from django.urls import path
<<<<<<< HEAD
from . import views # Importa todas las vistas desde la misma aplicación asistencia

urlpatterns = [
    # URLs para navegación general y autenticación
    path('', views.home, name='home'), # Página de inicio (root de la app asistencia)
    path('login/', views.user_login_view, name='login'), # Iniciar sesión para usuarios normales
    path('login_experto/', views.login_experto, name='login_experto'), # Iniciar sesión para expertos
    path('principal/', views.principal, name='principal'), # Página principal del cliente (dashboard)
    path('registrarse/', views.registrarse_view, name='registrarse'), # Registro de usuarios (cambiado a registrarse_view)
    path('regisexperto/', views.regisexperto, name='regisexperto'), # Registro de expertos
    path('modificar/', views.editar_perfil_view, name='perfil'), # Edición de perfil (cambiado a editar_perfil_view y name='perfil')



    # URLs para funcionalidades de búsqueda y administración
    path('busc_experto/', views.busc_experto, name='busc_experto'), # Búsqueda de expertos
    path('admin_principal/', views.admin_principal, name='admin_principal'), # Dashboard del administrador
    path('solicitudes_admin/', views.solicitudes_admin, name='solicitudes_admin'), # Gestión de solicitudes por el admin
    path('login_admin/', views.login_admin, name='login_admin'), # Login para administradores

    # URLs relacionadas con servicios y reservas
    path('servicioAceptado/', views.servicioAceptado, name='servicioAceptado'), # Vista de servicio aceptado
    path('servicioAceptadoexpe/', views.servicioAceptadoexpe, name='servicioAceptadoexpe'), # Vista de servicio aceptado para experto
    path('chat/', views.chat, name='chat'), # Página de chat
    path('servicioCancelado/', views.servicioCancelado, name='servicioCancelado'), # Vista de servicio cancelado
    path('servicioCanceladoexpe/', views.servicioCanceladoexpe, name='servicioCanceladoexpe'), # Vista de servicio cancelado para experto
    path('reserva/', views.reserva, name='reserva'), # Página de reserva de servicios


    # URLs para términos legales y documentación
    path('terminos-condiciones/', views.terminos_condiciones, name='terminos_condiciones'), # Términos y condiciones
    path('tratamiento-datos/', views.tratamiento_datos, name='tratamiento_datos'), # Tratamiento de datos
    path('experto/', views.experto, name='experto'), # Página de experto (dashboard o perfil general)
    path('historial_experto/', views.historial_experto, name='historial_experto'), # Historial de servicios del experto

    # URLs para documentación del proyecto (bases de datos, diagramas, etc.)
    path('fin/', views.fin, name='fin'), # ¿Fin de qué? (revisar nombre)
=======
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login_view, name='login'),
    path('logout/', views.user_logout_view, name='logout'), # ¡Añade esta línea!
    path('login_experto/', views.login_experto, name='login_experto'),
    path('login_admin/', views.login_admin, name='login_admin'),
    path('principal/', views.principal, name='principal'),
    path('busc_experto/', views.busc_experto, name='busc_experto'),
    path('admin_principal/', views.admin_principal, name='admin_principal'),
    path('solicitudes_admin/', views.solicitudes_admin, name='solicitudes_admin'),
    path('modificar/', views.modificar, name='modificar'),
    path('servicioAceptado/', views.servicioAceptado, name='servicioAceptado'),
    path('servicioAceptadoexpe/', views.servicioAceptadoexpe, name='servicioAceptadoexpe'),
    path('chat/', views.chat, name='chat'),
    path('servicioCancelado/', views.servicioCancelado, name='servicioCancelado'),
    path('servicioCanceladoexpe/', views.servicioCanceladoexpe, name='servicioCanceladoexpe'),
    path('registrarse/', views.registrarse, name='registrarse'),
    path('regisexperto/', views.regisexperto, name='regisexperto'),
    path('terminos-condiciones/', views.terminos_condiciones, name='terminos_condiciones'),
    path('tratamiento-datos/', views.tratamiento_datos, name='tratamiento_datos'),
    path('experto/', views.experto, name='experto'),
    path('historial_experto/', views.historial_experto, name='historial_experto'),
    path('fin/', views.fin, name='fin'),
>>>>>>> origin/master
    path('normalizacion/', views.normalizacion, name='normalizacion'),
    path('modelo_relacional/', views.modelo_relacional, name='modelo_relacional'),
    path('sentenciasddl/', views.sentenciasddl, name='sentenciasddl'),
    path('sentencias_dml/', views.sentencias_dml, name='sentencias_dml'),
    path('diccionario_de_datos/', views.diccionario_de_datos, name='diccionario_de_datos'),
    path('diagrama_de_clases/', views.diagrama_de_clases, name='diagrama_de_clases'),
<<<<<<< HEAD

    # URL de éxito para el registro (si aún la necesitas, si no, puedes eliminarla)
    path('registro-exitoso/', views.registro_exitoso, name='registro_exitoso'),
=======
    path('reserva/', views.reserva, name='reserva'),

>>>>>>> origin/master
]