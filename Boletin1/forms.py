from django import forms
from django.core.exceptions import ValidationError

DIAS_SEMANA = [
    ('lunes', 'Lunes'),
    ('martes', 'Martes'),
    ('miércoles', 'Miércoles'),
    ('jueves', 'Jueves'),
    ('viernes', 'Viernes'),
    ('sábado', 'Sábado'),
    ('domingo', 'Domingo'),
]

class formulario(forms.Form):
    fechaInicio = forms.DateField(
        label='fIni',
        required=True,
        help_text='Ingrese la fecha inicial.',
        input_formats=['%d/%m/%Y'],
        widget=forms.TextInput(attrs={'placeholder': 'dd/mm/YYYY'})
    )
    fechaFin = forms.DateField(
        label='fFin',
        required=True,
        help_text='Ingrese la ficha final.',
        input_formats=['%d/%m/%Y'],
        widget=forms.TextInput(attrs={'placeholder': 'dd/mm/YYYY'})
    )
    dias = forms.MultipleChoiceField(
        label='Dias',
        choices=DIAS_SEMANA,
        widget=forms.CheckboxSelectMultiple,
        required=True,
        help_text='Ingrese los días de la semana, de 1 a 3.'
    )
    correoElectronico = forms.EmailField(
        label='email',
        required=True,
        help_text='Ingrese su dirección de correo electrónico válida.'
    )

    def clean(self):
        cleaned_data = super().clean()
        fechaInicio = cleaned_data.get("fechaInicio")
        fechaFin = cleaned_data.get("fechaFin")
        dias = cleaned_data.get("dias")
        correoElectronico = cleaned_data.get("correoElectronico")

        if not dias:
            raise ValidationError("Seleccione al menos un día de la semana.")

        if len(dias) > 3:
            raise ValidationError("Seleccione no más de tres días de la semana.")
        
        if not correoElectronico.endswith("@iesmartinezm.es"):
            raise ValidationError("El correo electrónico debe terminar en '@iesmartinezm.es'.")

        return cleaned_data

    