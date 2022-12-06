from django import forms
from evaApp.models import Trabajador
from consolaApp.models import Consola
from django.contrib.admin import widgets
from django.core import validators 
from django.forms import ValidationError


class FormTrabajador(forms.ModelForm):
        
        consolas = Consola.objects.values('nombreConsola')
        test = {consolas}
        # print(f'test {test}')
        tupla = tuple()
        

        print(tupla)
        i = 0
        k= 0
        for consola1 in test:
            for campo in consola1:
                print(consola1[i]['nombreConsola'])
                print(consola1[0])
                print (f'tuplaaaaaaaaa {tupla}')
                
                
                i+=1
                

        # for i in consolas:
            # tpl = (i,consolas[i])
            # tupla.append(tpl)
            # print(tupla)
        # hola = list(test.values())
        # print(f'holaaaaa: {hola}')
        
        # test = {
        #     "hola": "1",
        #     "bien": "2"
        # }
        # for claves in test:
        #     print(f'clavessss {test[claves]}')

        print("separador")
        # print(f'hola: {test}')
        rut             = forms.CharField(min_length=10, max_length=10)
        nombre          = forms.CharField()
        apellido        = forms.CharField()
        telefono        = forms.IntegerField()
        correo          = forms.CharField()
        compraConsola   = forms.CharField(widget=forms.Select(choices="consola1"))


        rut.widget.attrs['class'] = 'form-control'
        nombre.widget.attrs['class'] = 'form-control'
        apellido.widget.attrs['class'] = 'form-control'
        telefono.widget.attrs['class'] = 'form-control'
        correo.widget.attrs['class'] = 'form-control'
        compraConsola.widget.attrs['class'] = 'form-control'


        rut.widget.attrs['placeholder'] = '12.235.678-k'
        correo.widget.attrs['placeholder'] = 'Example@gmail.com'
        telefono.widget.attrs['placeholder'] = 'X XXXX XXXX'

        def clean_rut(self):
            rut = self.cleaned_data.get('rut')
            existe = Trabajador.objects.filter(rut__iexact=rut).exists()
            if existe:
                raise ValidationError("El rut ya existe")
            if rut.find("-") == -1 :
                raise  forms.ValidationError('El rut debe contener un "-". Ej: 12.235.678-k ')
            if len(rut) != 10:
                print("rut no valido")
                raise  forms.ValidationError('El rut debe tener un minimo de 10 caracteres. Ej: 12.235.678-k')
            return rut

        def clean_correo(self):
            correo = self.cleaned_data.get('correo')
            if correo.find('@') == -1:
                print("El correo debe contener un  @")
                raise forms.ValidationError("El correo debe contener un  @")
            if correo.find(".com") == -1 :
                raise forms.ValidationError("El correo debe tener una extension '.com'")
            return correo

        class Meta:
            model = Trabajador
            fields = '__all__'  #['rut','nombre','apellido','apellido','telefono','correo',]# incluye todo lo que esta en el modelo
            widgets = {
                "fechaNacimiento" : forms.SelectDateWidget(years=range(1940,2022)),
            }