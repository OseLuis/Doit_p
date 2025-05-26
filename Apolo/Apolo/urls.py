from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # URLs del administrador de Django
    path('admin/', admin.site.urls),

    # Incluye las URLs de tu aplicación 'asistencia'
    # Esto hará que todas las URLs definidas en asistencia/urls.py
    # estén disponibles también desde la raíz del sitio.
    path('', include('asistencia.urls')), # ¡Esta es la línea clave que faltaba!

    # Nota: Si ya usas `path('', include('asistencia.urls'))`
    # y quieres que todas tus URLs de 'asistencia' estén en la raíz,
    # entonces la línea `path('asistencia/', include('asistencia.urls'))`
    # se vuelve redundante y puedes eliminarla para evitar confusiones
    # o posibles conflictos de nombres si alguna vez creas otra app.
    # Por ahora, puedes dejarla si quieres que /asistencia/ también funcione,
    # pero el acceso principal será sin el prefijo /asistencia/.
    # Mi recomendación es eliminar la redundante si quieres que la raíz sea tu app.
]