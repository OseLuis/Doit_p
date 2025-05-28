# asistencia/views.py

from django.shortcuts import render, redirect
<<<<<<< HEAD
from django.contrib.auth import login, logout # ¡IMPORTA login Y logout correctamente!
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy # ¡IMPORTA reverse_lazy para las redirecciones!


from .forms import RegistroForm, PerfilUsuarioForm

# --- VISTAS DE AUTENTICACIÓN Y PERFIL ---

# Vista de registro de usuario (NORMAL)
def registrarse_view(request):
=======
from django.urls import reverse_lazy
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate # ¡Importa 'authenticate' aquí!
from django.contrib.auth.forms import AuthenticationForm # ¡Importa AuthenticationForm!
from .forms import RegistroForm
from django.contrib.auth.decorators import login_required


# --- Vistas protegidas con @login_required ---

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def principal(request): # Esta es la vista que renderiza principal.html
    return render(request, 'principal.html')

@login_required
def busc_experto(request):
    return render(request, 'busc_experto.html')

@login_required
def modificar(request):
    return render(request, 'modificar.html')

@login_required
def servicioAceptado(request):
    return render(request, 'servicioAceptado.html')

@login_required
def servicioAceptadoexpe(request):
    return render(request, 'servicioAceptadoexpe.html')

@login_required
def chat(request):
    return render(request, 'chat.html')

@login_required
def servicioCancelado(request):
    return render(request, 'servicioCancelado.html')

@login_required
def servicioCanceladoexpe(request):
    return render(request, 'servicioCanceladoexpe.html')

@login_required
def experto(request):
    return render(request, 'experto.html')

@login_required
def historial_experto(request):
    return render(request, 'historial_experto.html')

@login_required
def fin(request):
    return render(request, 'fin.html')

@login_required
def normalizacion(request):
    return render(request, 'normalizacion.html')

@login_required
def modelo_relacional(request):
    return render(request, 'modelo_relacional.html')

@login_required
def sentenciasddl(request):
    return render(request, 'sentenciasddl.html')

@login_required
def sentencias_dml(request):
    return render(request, 'sentencias_dml.html')

@login_required
def diccionario_de_datos(request):
    return render(request, 'diccionario_de_datos.html')

@login_required
def diagrama_de_clases(request):
    return render(request, 'diagrama_de_clases.html')

@login_required
def admin_principal(request):
    return render(request, 'admin_principal.html')

@login_required
def solicitudes_admin(request):
    return render(request, 'solicitudes_admin.html')

@login_required
def reserva(request):
    return render(request, 'reserva.html')

# --- Vistas de Autenticación y Registro (NO deben tener @login_required) ---

def user_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            # Redirige al 'next' parámetro si existe, de lo contrario a 'principal'
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            return redirect(reverse_lazy('principal'))
        # Si el formulario no es válido, se renderizará con errores
    else:
        form = AuthenticationForm()
    return render(request, 'sign-in/login.html', {'form': form})

def user_logout_view(request):
    auth_logout(request)
    # Redirige a la página de inicio o a la página de login después de cerrar sesión
    return redirect(reverse_lazy('home')) # O 'login' si prefieres

def login_experto(request):
    # Aquí podrías tener una lógica de login específica para expertos
    # que, por ejemplo, valide el tipo de usuario después de la autenticación estándar.
    # Usaremos AuthenticationForm, y luego podríamos verificar el tipo de usuario si aplica.
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            # Si tienes un campo 'tipo_usuario' en tu modelo de usuario personalizado
            # puedes verificarlo aquí. Asegúrate de que tu modelo CustomUser tenga 'tipo_usuario'.
            if hasattr(user, 'tipo_usuario') and user.tipo_usuario == 'experto':
                auth_login(request, user)
                next_url = request.GET.get('next')
                if next_url:
                    return redirect(next_url)
                return redirect(reverse_lazy('experto')) # Redirige a la página de experto
            else:
                form.add_error(None, "Las credenciales no corresponden a un experto.")
        # Si el formulario no es válido o el tipo de usuario no es correcto
        return render(request, 'sign-in/login_experto.html', {'form': form})
    else:
        form = AuthenticationForm()
    return render(request, 'sign-in/login_experto.html', {'form': form})


def login_admin(request):
    # Similar a login_experto, podrías añadir lógica específica para administradores.
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            # Si tienes un campo 'tipo_usuario' en tu modelo de usuario personalizado
            if hasattr(user, 'tipo_usuario') and user.tipo_usuario == 'admin': # Asumiendo 'admin' como valor
                auth_login(request, user)
                next_url = request.GET.get('next')
                if next_url:
                    return redirect(next_url)
                return redirect(reverse_lazy('admin_principal')) # Redirige a la página de admin
            else:
                form.add_error(None, "Las credenciales no corresponden a un administrador.")
        # Si el formulario no es válido o el tipo de usuario no es correcto
        return render(request, 'sign-in/login_admin.html', {'form': form})
    else:
        form = AuthenticationForm()
    return render(request, 'sign-in/login_admin.html', {'form': form})


# --- Vistas de Registro (NO deben tener @login_required) ---
def registrarse(request):
>>>>>>> origin/master
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
<<<<<<< HEAD
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
=======
            auth_login(request, user) # Inicia sesión al usuario recién registrado
            return redirect(reverse_lazy('principal'))
        else:
            print(form.errors) # Esto te ayudará a depurar si el formulario no es válido
    else:
        form = RegistroForm(initial={'tipo_usuario': 'usuario'})
    return render(request, 'registrarse.html', {'form': form})

>>>>>>> origin/master
def regisexperto(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
<<<<<<< HEAD
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
=======
            user = form.save(commit=False)
            user.tipo_usuario = 'experto' # Asegúrate de que este campo exista en tu modelo de usuario
            user.save()
            auth_login(request, user) # Inicia sesión al experto recién registrado
            return redirect(reverse_lazy('principal')) # Podrías redirigir a 'experto'
        else:
            print(form.errors)
    else:
        form = RegistroForm(initial={'tipo_usuario': 'experto'})
    return render(request, 'regisexperto.html', {'form': form})

# --- Otras vistas públicas (NO deben tener @login_required) ---
def nosotros(request):
    return render(request, 'nosotros.html')
>>>>>>> origin/master

def terminos_condiciones(request):
    return render(request, 'terminos_condiciones.html')

def tratamiento_datos(request):
<<<<<<< HEAD
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
=======
    return render(request, 'tratamiento_datos.html')
>>>>>>> origin/master
