from django import forms
from django.core.exceptions import ValidationError

class Imagen(forms.Form):
    imagen = forms.ImageField(upload_to='imagenes/')
    
class SubirImagenForm(forms.ModelForm):
    class Meta:
        model = Imagen
        fields = ['imagen']

    def clean_imagen(self):
        imagen = self.cleaned_data.get('imagen')

        # Validar la extensión del archivo
        extensiones_permitidas = ['jpg', 'jpeg', 'png']
        if not any(imagen.name.lower().endswith(ext) for ext in extensiones_permitidas):
            raise forms.ValidationError('La imagen debe tener una extensión jpg o png.')

        # Validar el tamaño del archivo
        tamaño_maximo = 50 * 1024  # 50 KB
        if imagen.size > tamaño_maximo:
            raise forms.ValidationError('La imagen no puede ser mayor a 50 KB.')

        return imagen