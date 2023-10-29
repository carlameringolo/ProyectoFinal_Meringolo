from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView,UpdateView,CreateView
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm,UserChangeForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.


def inicio(req):
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
    fields=['nombre','apellido', 'aptoFisico']
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
class ClasesList(LoginRequiredMixin,ListView):
    model=Clases
    template_name='clases_list.html'
    context_object_name='clases'


class ClasesDetail(DetailView):
    model=Clases
    template_name='clases_detail.html'
    context_object_name='clases'

class ClasesCreate(CreateView):
    model=Clases
    template_name='clases_create.html'
    fields=['nombre','duracion', 'dificultad']
    success_url='/app-coder/listaClases'

class ClasesUpdate(UpdateView):
    model=Clases
    template_name='clases_update.html'
    fields=('__all__')
    context_object_name='clases'
    success_url='/app-coder/listaClases'

class ClasesDelete(DeleteView):
    model=Clases
    template_name='clases_delete.html'
    context_object_name='clases'
    success_url='/app-coder/listaClases'





#SEDES
class SedesList(LoginRequiredMixin,ListView):
    model=Sede
    template_name='sedes_list.html'
    context_object_name='sedes'


class SedesDetail(DetailView):
    model=Sede
    template_name='sedes_detail.html'
    context_object_name='sedes'

class SedesCreate(CreateView):
    model=Sede
    template_name='sedes_create.html'
    fields=['localidad','telefono', 'apertura']
    success_url='/app-coder/listaSedes'

class SedesUpdate(UpdateView):
    model=Sede
    template_name='sedes_update.html'
    fields=('__all__')
    context_object_name='sedes'
    success_url='/app-coder/listaSedes'

class SedesDelete(DeleteView):
    model=Sede
    template_name='sedes_delete.html'
    context_object_name='sedes'
    success_url='/app-coder/listaSedes'



