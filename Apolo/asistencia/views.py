# asistencia/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout # ¡IMPORTA login Y logout correctamente!
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy # ¡IMPORTA reverse_lazy para las redirecciones!


from .forms import RegistroForm, PerfilUsuarioForm

# --- VISTAS DE AUTENTICACIÓN Y PERFIL ---

# Vista de registro de usuario (NORMAL)
def registrarse_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Usa la función 'login' importada de django.contrib.auth
            messages.success(request, '¡Registro exitoso! Has iniciado sesión.')
            print("Registro exitoso. Redirigiendo a 'principal'") # Mensaje de depuración
            # Redirige a la página principal después de un registro exitoso
            return redirect('principal') # Usamos el 'name' de la URL principal
        else:
            # --- ¡AÑADIDA ESTA LÍNEA PARA VER LOS ERRORES DEL FORMULARIO! ---
            print("El formulario no es válido. Errores:", form.errors)
            messages.error(request, 'Hubo un error en el registro. Por favor, corrige los errores y revisa la consola del servidor.')
    else:
        form = RegistroForm(initial={'tipo_usuario': 'usuario'}) # Asegura que el tipo_usuario sea 'usuario' por defecto
    return render(request, 'registrarse.html', {'form': form})

# Vista de registro de experto
def regisexperto(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False) # Guarda el usuario pero no lo persiste en la DB aún
            user.tipo_usuario = 'experto' # Asigna el rol de experto
            user.save() # Ahora sí guarda el usuario con el rol asignado

            login(request, user) # Usa la función 'login' importada
            messages.success(request, '¡Registro de experto exitoso! Has iniciado sesión.')
            return redirect('experto') # Redirige a la página de experto después del registro
        else:
            messages.error(request, 'Hubo un error en el registro de experto. Por favor, corrige los errores.')
            print("El formulario de experto no es válido. Errores:", form.errors) # También para experto
    else:
        form = RegistroForm(initial={'tipo_usuario': 'experto'}) # Asegura que el tipo_usuario sea 'experto'
    return render(request, 'regisexperto.html', {'form': form}) # Asumo que tienes una plantilla regisexperto.html

# Vista para editar perfil
@login_required
def editar_perfil_view(request):
    user = request.user
    if request.method == 'POST':
        form = PerfilUsuarioForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Tu perfil ha sido actualizado con éxito!')
            return redirect('perfil') # Redirige a la misma página de perfil o a donde quieras
        else:
            messages.error(request, 'Hubo un error al actualizar tu perfil. Por favor, revisa los datos.')
            print("El formulario de perfil no es válido. Errores:", form.errors) # Para edición de perfil
    else:
        form = PerfilUsuarioForm(instance=user)
    return render(request, 'modificar.html', {'form': form})

# Vista para cerrar sesión
def user_logout_view(request):
    logout(request)
    messages.info(request, 'Has cerrado sesión correctamente.')
    return redirect('home') # Redirige a la página de inicio después del logout

# --- VISTAS GENERALES DE LA APLICACIÓN ---

def home(request):
    return render(request, 'home.html')

def principal(request):
    return render(request, 'principal.html')

def busc_experto(request):
    return render(request, 'busc_experto.html')

def servicioAceptado(request):
    return render(request, 'servicioAceptado.html')

def servicioAceptadoexpe(request):
    return render(request, 'servicioAceptadoexpe.html')

def chat(request):
    return render(request, 'chat.html')

def servicioCancelado(request):
    return render(request, 'servicioCancelado.html')

def servicioCanceladoexpe(request):
    return render(request, 'servicioCanceladoexpe.html')

def experto(request):
    return render(request, 'experto.html')

def historial_experto(request):
    return render(request, 'historial_experto.html')

def fin(request):
    return render(request, 'fin.html')

def normalizacion(request):
    return render(request, 'normalizacion.html')

def modelo_relacional(request):
    return render(request, 'modelo_relacional.html')

def sentenciasddl(request):
    return render(request, 'sentenciasddl.html')

def sentencias_dml(request):
    return render(request, 'sentencias_dml.html')

def diccionario_de_datos(request):
    return render(request, 'diccionario_de_datos.html')

def diagrama_de_clases(request):
    return render(request, 'diagrama_de_clases.html')

def reserva(request):
    return render(request, 'reserva.html')

def terminos_condiciones(request):
    return render(request, 'terminos_condiciones.html')

def tratamiento_datos(request):
    return render(request, 'tratamiento_datos.html')

# --- VISTAS DE LOGIN (Ajusta según tus templates) ---
def user_login_view(request):
    # Esto es solo un placeholder, reemplaza con tu lógica de login real
    # de Django (ej. AuthenticationForm)
    return render(request, 'sign-in/login.html')

def login_experto(request):
    # Placeholder
    return render(request, 'sign-in/login_experto.html')

def login_admin(request):
    # Placeholder
    return render(request, 'sign-in/login_admin.html')

def admin_principal(request):
    return render(request, 'admin_principal.html')

def solicitudes_admin(request):
    return render(request, 'solicitudes_admin.html')

# --- VISTA DE ÉXITO DE REGISTRO (si aún la usas) ---
def registro_exitoso(request):
    return render(request, 'registro_exitoso.html')