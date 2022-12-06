from django.shortcuts import render, redirect, get_object_or_404
from consolaApp.forms import FormConsola
from consolaApp.models import Consola
from django.contrib import messages

# Create your views here.
def listadoConsolas(request):
    consolas = Consola.objects.all()
    data = {'consolas': consolas}
    return render (request, 'consolaApp/Consolas.html',data)

def agregarConsola(request):
    data = {'form' : FormConsola}
    if request.method == 'POST':
        form = FormConsola(data=request.POST) #rellena formulario
        if form.is_valid():
            form.save()
            messages.success(request, "CONSOLA REGISTRADA")
            return redirect('../consolas')
        else: #si no es valido sobreescribe el form
            data["form"] = form
    return render (request, 'consolaApp/agregarConsola.html',data)

def eliminarConsola(request,id):
    consola = Consola.objects.get(id=id)
    consola.delete()
    messages.success(request, "CONSOLA ELIMINADA")
    return redirect('../consolas')

def actualizarConsola(request,id):
    consola = get_object_or_404(Consola, id=id)
    form  = FormConsola(instance=consola)
    if request.method == 'POST':
        form = FormConsola(request.POST, instance=consola) #instance rellena el formulario
        if form.is_valid():
            form.save()
            messages.success(request, "CONSOLA MODIFICADA")
            return redirect('../consolas')
        # else:
        #     data["form"] = form #en caso de un error de requisito reenvia el form
    data = {'form' : form}
    return render(request, 'consolaApp/modificarConsola.html',data)