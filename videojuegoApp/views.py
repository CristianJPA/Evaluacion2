from django.shortcuts import render, redirect, get_object_or_404
from videojuegoApp.forms import FormVideojuego
from videojuegoApp.models import Videojuego
from django.contrib import messages

# Create your views here.
def listadoVideojuegos(request):
    videojuegos = Videojuego.objects.all()
    data = {'videojuegos': videojuegos}
    return render (request, 'videojuegosApp/Videojuegos.html',data)

def agregarVideojuego(request):
    data = {'form' : FormVideojuego}
    if request.method == 'POST':
        form = FormVideojuego(data=request.POST) #rellena formulario
        if form.is_valid():
            form.save()
            messages.success(request, "VIDEOJUEGO REGISTRADO")
            return redirect('../videojuegos')
        else: #si no es valido sobreescribe el form
            data["form"] = form
    return render (request, 'videojuegosApp/agregarVideojuego.html',data)

def eliminarVideojuego(request,id):
    videojuegos = Videojuego.objects.get(id=id)
    videojuegos.delete()
    messages.success(request, "VIDEOJUEGO ELIMINADO")
    return redirect('../videojuegos')

def actualizarVideojuego(request,id):
    videojuegos = get_object_or_404(Videojuego, id=id)
    form  = FormVideojuego(instance=videojuegos)
    if request.method == 'POST':
        form = FormVideojuego(request.POST, instance=videojuegos) #instance rellena el formulario
        if form.is_valid():
            form.save()
            messages.success(request, "VIDEOJUEGO MODIFICADO")
            return redirect('../videojuegos')
        # else:
        #     data["form"] = form #en caso de un error de requisito reenvia el form
    data = {'form' : form}
    return render(request, 'videojuegosApp/modificarVideojuego.html',data)