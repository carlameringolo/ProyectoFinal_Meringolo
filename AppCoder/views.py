from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView,UpdateView,CreateView
from .models import *
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from operator import attrgetter
from .forms import *

# Create your views here.


def inicio(req):
    try:
        avatar=Avatar.objects.get(user=req.user.id)
        return render(req, 'inicio.html',{'url_avatar': avatar.imagen.url})
    except:
        return render(req, 'inicio.html')



#ENTRENADOR
class EntrenadorList(LoginRequiredMixin,ListView):
    model=Entrenador
    template_name='entrenador_list.html'
    context_object_name='entrenadores'


class EntrenadorDetail(DetailView):
    model=Entrenador
    template_name='entrenador_detail.html'
    context_object_name='entrenador'

class EntrenadorCreate(CreateView):
    model=Entrenador
    template_name='entrenador_create.html'
    fields=['nombre','apellido', 'especialidad']
    success_url='/app-coder/listaEntrenadores'



class EntrenadorUpdate(UpdateView):
    model=Entrenador
    template_name='entrenador_update.html'
    fields=('__all__')
    context_object_name='entrenador'
    success_url='/app-coder/listaEntrenadores'

class EntrenadorDelete(DeleteView):
    model=Entrenador
    template_name='entrenador_delete.html'
    context_object_name='entrenador'
    success_url='/app-coder/listaEntrenadores'




#CLIENTE
class ClienteList(LoginRequiredMixin,ListView):
    model=Cliente
    template_name='cliente_list.html'
    context_object_name='clientes'


class ClienteDetail(DetailView):
    model=Cliente
    template_name='cliente_detail.html'
    context_object_name='cliente'

class ClienteCreate(CreateView):
    model=Cliente
    template_name='cliente_create.html'
    fields=['nombre','apellido','dni', 'aptoFisico']
    success_url='/app-coder/listaClientes'

class ClienteUpdate(UpdateView):
    model=Cliente
    template_name='cliente_update.html'
    fields=('__all__')
    context_object_name='cliente'
    success_url='/app-coder/listaClientes'

class ClienteDelete(DeleteView):
    model=Cliente
    template_name='cliente_delete.html'
    context_object_name='cliente'
    success_url='/app-coder/listaClientes'





#CLASES
class ClasesList(ListView):
    model=Clases
    template_name='clases_list.html'
    context_object_name='clases'


class ClasesDetail(DetailView):
    model=Clases
    template_name='clases_detail.html'
    context_object_name='clase'

class ClasesCreate(CreateView):
    model=Clases
    template_name='clases_create.html'
    fields=['nombre','duracion', 'dificultad']
    success_url='/app-coder/listaClases'

class ClasesUpdate(UpdateView):
    model=Clases
    template_name='clases_update.html'
    fields=('__all__')
    context_object_name='clase'
    success_url='/app-coder/listaClases'

class ClasesDelete(DeleteView):
    model=Clases
    template_name='clases_delete.html'
    context_object_name='clase'
    success_url='/app-coder/listaClases'





#SEDES
class SedesList(ListView):
    model=Sede
    template_name='sede_list.html'
    context_object_name='sedes'


class SedesDetail(DetailView):
    model=Sede
    template_name='sede_detail.html'
    context_object_name='sede'

class SedesCreate(CreateView):
    model=Sede
    template_name='sede_create.html'
    fields=['localidad','telefono', 'apertura']
    success_url='/app-coder/listaSedes'

class SedesUpdate(UpdateView):
    model=Sede
    template_name='sede_update.html'
    fields=('__all__')
    context_object_name='sede'
    success_url='/app-coder/listaSedes'

class SedesDelete(DeleteView):
    model=Sede
    template_name='sede_delete.html'
    context_object_name='sede'
    success_url='/app-coder/listaSedes'




def calendario_view(req):
    clases=Clases.objects.all()
    clases=sorted(clases, key=attrgetter('hora_inicio'))
    todas_clases=[]

    for clase in clases:
        todas_clases.append({
            'nombre':clase.nombre,
            'hora_inicio':clase.hora_inicio,
            'dia':clase.dia
        })
    
    context={
        'clases':todas_clases,
        'dias_semana':['Lunes','Martes','Miercoles','Jueves','Viernes','Sabado']
    }

    return render(req, 'calendario.html',context)



def loginView(req):

    if req.method == 'POST':
        miFormulario=AuthenticationForm(req, data=req.POST)
        
        if miFormulario.is_valid():

            data=miFormulario.cleaned_data
            usuario= data['username']
            psw= data['password']
            user=authenticate(username=usuario, password=psw)

            if user:
                login(req,user)
                return render(req, 'inicio.html', {'mensaje': f'Bienvenido {usuario}!'})
            else:
                return render(req, 'inicio.html', {'mensaje': f'Datos incorrectos'})
            
    else:
        miFormulario=AuthenticationForm()

    return render(req, 'login.html',{'miFormulario':miFormulario})



def register(req):

    if req.method == 'POST':
        miFormulario=UserCreationForm(req.POST)
        
        if miFormulario.is_valid():

            data=miFormulario.cleaned_data
            usuario= data['username']
            miFormulario.save()
            return render(req,'inicio.html',{'mensaje':f'Usuario {usuario} creado con exito'})
    else:
        miFormulario=UserCreationForm()
    return render(req, 'registro.html',{'miFormulario':miFormulario})




@login_required(login_url='Login')
def editar_perfil(req):
    
    usuario= req.user

    if req.method == 'POST':
        
        miFormulario=UserEditForm(req.POST,instance=req.user)
        
        if miFormulario.is_valid():

            data=miFormulario.cleaned_data

            usuario.first_name=data['first_name']
            usuario.last_name=data['last_name']
            usuario.email=data['email']
            usuario.save()

            context={
                'first_name':usuario.first_name,
                'last_name':usuario.last_name,
                'email':usuario.email
            }

            return render(req,'perfil_actualizado.html',context)

    else:
        miFormulario=UserEditForm()

    if not req.user.is_authenticated:
        return render(req, 'login.html',{'miFormulario':miFormulario})
    
    return render(req, 'editarPerfil.html',{'miFormulario':miFormulario})



@login_required(login_url='Login')
def agregar_avatar(req):

    if req.method == 'POST':
        
        miFormulario=AvatarFormulario(req.POST, req.FILES)
        
        if miFormulario.is_valid():

            data=miFormulario.cleaned_data

            avatar=Avatar(user=req.user, imagen=data['imagen'])
            avatar.save()

            return render(req,'inicio.html',{'mensaje':'Avatar actualizados con exito'})
    else:
        miFormulario=AvatarFormulario()
        return render(req,'agregarAvatar.html',{'miFormulario':miFormulario})



def acerca_de_mi(req):
    return render(req, 'acerca_de_mi.html')



def contacto(req):
    formulario=ComentarioFormulario()

    if req.method=='POST':
        formulario=ComentarioFormulario(req.POST)
        if formulario.is_valid():
            formulario.save()
            return render(req,'inicio.html',{'mensaje':'Mensaje enviado con exito'})
    return render(req,'contacto.html',{'formulario':formulario})
 
