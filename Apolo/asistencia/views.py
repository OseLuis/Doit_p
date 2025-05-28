# asistencia/views.py

from django.shortcuts import render, redirect
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
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user) # Inicia sesión al usuario recién registrado
            return redirect(reverse_lazy('principal'))
        else:
            print(form.errors) # Esto te ayudará a depurar si el formulario no es válido
    else:
        form = RegistroForm(initial={'tipo_usuario': 'usuario'})
    return render(request, 'registrarse.html', {'form': form})

def regisexperto(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
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

def terminos_condiciones(request):
    return render(request, 'terminos_condiciones.html')

def tratamiento_datos(request):
    return render(request, 'tratamiento_datos.html')