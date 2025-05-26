# asistencia/forms.py (Fragmento importante)

from django import forms
from .models import CustomUser, Genero
from django.contrib.auth.forms import UserCreationForm

class RegistroForm(UserCreationForm):
    genero = forms.ModelChoiceField(
        queryset=Genero.objects.all().order_by('nombre'),
        empty_label="Selecciona tu género",
        required=False, # Si es opcional
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    # ... (El resto de tus campos personalizados como tipo_usuario, nacionalidad, numDoc, etc.)
    # Asegúrate de que todos los campos que quieres guardar estén aquí.
    # Los que ya están en AbstractUser (username, password, email, first_name, last_name)
    # pueden no necesitar ser definidos explícitamente a menos que quieras personalizar su widget o validación.

    # Ejemplo de un campo personalizado, como tipo_usuario
    tipo_usuario_choices = [
        ('usuario', 'Usuario'),
        ('experto', 'Experto'),
    ]
    tipo_usuario = forms.ChoiceField(
        choices=tipo_usuario_choices,
        initial='usuario',
        label="Tipo de Usuario",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    nacionalidad = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    numDoc = forms.CharField(max_length=100, required=False, label="Número de Documento", widget=forms.TextInput(attrs={'class': 'form-control'}))
    telefono = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fechaNacimiento = forms.DateField(required=False, label="Fecha de Nacimiento", widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    # Aquí puedes añadir email si quieres controlarlo, sino UserCreationForm lo maneja
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    evidenciaTrabajo = forms.CharField(max_length=200, required=False, label="Evidencia de Trabajo (URL/Descripción)", widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))
    experienciaTrabajo = forms.CharField(required=False, label="Experiencia de Trabajo", widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))
    hojaVida = forms.CharField(max_length=300, required=False, label="Link Hoja de Vida", widget=forms.TextInput(attrs={'class': 'form-control'}))


    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + (
            'first_name', 'last_name', 'email', # Incluye email si lo definiste arriba
            'genero', 'tipo_usuario', 'nacionalidad', 'numDoc', 'telefono', 'fechaNacimiento',
            'evidenciaTrabajo', 'experienciaTrabajo', 'hojaVida',
        )
        labels = {
            'username': 'Nombre de Usuario',
            'first_name': 'Nombres',
            'last_name': 'Apellidos',
            'email': 'Correo Electrónico',
        }

    # ¡Este es el método clave que guarda los datos!
    def save(self, commit=True):
        user = super().save(commit=False) # Llama al save de UserCreationForm (guarda username, password hasheada)

        # Asigna los campos personalizados desde cleaned_data a la instancia del usuario
        user.genero = self.cleaned_data.get('genero')
        user.tipo_usuario = self.cleaned_data.get('tipo_usuario')
        user.nacionalidad = self.cleaned_data.get('nacionalidad')
        user.numDoc = self.cleaned_data.get('numDoc')
        user.telefono = self.cleaned_data.get('telefono')
        user.fechaNacimiento = self.cleaned_data.get('fechaNacimiento')
        user.evidenciaTrabajo = self.cleaned_data.get('evidenciaTrabajo')
        user.experienciaTrabajo = self.cleaned_data.get('experienciaTrabajo')
        user.hojaVida = self.cleaned_data.get('hojaVida')

        if commit:
            user.save() # ¡Guarda la instancia completa en la base de datos!
        return user