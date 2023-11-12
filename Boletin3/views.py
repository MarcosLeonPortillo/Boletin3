from .forms import SubirImagenForm
from .forms import Imagen

def subir_imagen(request):
    if request.method == 'POST':
        form = SubirImagenForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('galeria')
    else:
        form = SubirImagenForm()

    return render(request, 'subir_imagen.html', {'form': form})

def galeria(request):
    imagenes = Imagen.objects.all()
    return render(request, 'galeria.html', {'imagenes': imagenes})