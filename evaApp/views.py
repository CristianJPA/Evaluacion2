from django.shortcuts import render, redirect, get_object_or_404
from evaApp.forms import FormTrabajador
from evaApp.models import Trabajador
from consolaApp.models import Consola
from consolaApp.forms import FormConsola
from . import forms
from django.contrib import messages


# Create your views here.
def index(request):
    return render (request, 'evaApp/index.html')

def listadoTrabajadores(request):
    # consolas = Consola.objects.values('memoria')
    trabajadores = Trabajador.objects.all()
    data = {'trabajadores': trabajadores}
    return render (request, 'evaApp/Trabajadores.html',data)

def agregarTrabajador(request):
    data = {'form' : FormTrabajador}    
    
    if request.method == 'POST':
        form = FormTrabajador(data=request.POST) #rellena formulario
        if form.is_valid():
            form.save()
            messages.success(request, "TRABAJADOR REGISTRADO")
            return redirect('../trabajadores')
        else: #si no es valido sobreescribe el form
            data["form"] = form
    return render (request, 'evaApp/agregarTrabajador.html',data)


def eliminarTrabajador(request,id):
    trabajador = Trabajador.objects.get(id=id)
    trabajador.delete()
    messages.success(request, "TRABAJADOR ELIMINADO")
    return redirect('../trabajadores')

def actualizarTrabajador(request,id):
    trabajador = get_object_or_404(Trabajador, id=id)
    form  = FormTrabajador(instance=trabajador)
    if request.method == 'POST':
        form = FormTrabajador(request.POST, instance=trabajador) #instance rellena el formulario
        if form.is_valid():
            form.save()
            messages.success(request, "TRABAJADOR MODIFICADO")
            return redirect('../trabajadores')
        # else:
        #     data["form"] = form #en caso de un error de requisito reenvia el form
    data = {'form' : form}
    return render(request, 'evaApp/modificarTrabajador.html',data)
