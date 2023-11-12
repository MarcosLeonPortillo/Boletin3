from django.shortcuts import render
from .forms import formulario
# Create your views here.

def index(request):
    return render(request, 'Boletin1/index.html')

def crea_formulario(request):
    # Si se ha enviado el formulario
    tablero_form = formulario()
    if request.method == 'GET':
        tablero_form = formulario(request.GET)
        # Ejecutamos la validación
        if tablero_form.is_valid():
            # Los datos se obtienen del diccionario cleaned_data
            fechaInicio = tablero_form.cleaned_data['fechaInicio']
            fechaFin = tablero_form.cleaned_data['fechaFin']
            dias = tablero_form.cleaned_data['dias']
            correoElectronico = tablero_form.cleaned_data['correoElectronico']
            return render(request, 'Boletin1/index.html',
                          {'fechaInicio': fechaInicio, 'fechaFin': fechaFin,
                           'dias': dias, 'correoElectronico': correoElectronico})
    # Si se pide la página por primera vez
    return render(request, 'Boletin1/index.html', {'form': tablero_form})