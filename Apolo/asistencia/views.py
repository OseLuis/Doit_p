# asistencia/views.py

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import login as auth_login
from .forms import RegistroForm

# --- Vistas existentes ---
def home(request):
    return render(request, 'home.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def principal(request): # Esta es la vista que renderiza principal.html
    return render(request, 'principal.html')

# ¡AGREGA ESTAS VISTAS FALTANTES!
def busc_experto(request):
    return render(request, 'busc_experto.html')

def modificar(request):
    return render(request, 'modificar.html')

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

# --- ¡CAMBIO AQUÍ! Renombra tu vista de login ---
def user_login_view(request):
    return render(request, 'sign-in/login.html')

def login_experto(request):
    return render(request, 'sign-in/login_experto.html')

def login_admin(request):
    return render(request, 'sign-in/login_admin.html')

def admin_principal(request):
    return render(request, 'admin_principal.html')

def solicitudes_admin(request):
    return render(request, 'solicitudes_admin.html')

# --- Vistas de Registro Actualizadas (Ya las tienes bien configuradas para redirigir a 'principal') ---
def registrarse(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect(reverse_lazy('principal'))
        else:
            print(form.errors)
    else:
        form = RegistroForm(initial={'tipo_usuario': 'usuario'})
    return render(request, 'registrarse.html', {'form': form})

def regisexperto(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.tipo_usuario = 'experto'
            user.save()

            auth_login(request, user)
            return redirect(reverse_lazy('principal'))
        else:
            print(form.errors)
    else:
        form = RegistroForm(initial={'tipo_usuario': 'experto'})
    return render(request, 'regisexperto.html', {'form': form})

# --- Otras vistas existentes ---
def terminos_condiciones(request):
    return render(request, 'terminos_condiciones.html')

def tratamiento_datos(request):
    return render(request, 'tratamiento_datos.html')

def reserva(request):
    return render(request, 'reserva.html')