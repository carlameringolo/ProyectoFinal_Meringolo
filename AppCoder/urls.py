from django.urls import path
from AppCoder.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicio, name='Inicio'),
    path('listaEntrenadores/', EntrenadorList.as_view(), name='ListarEntrenadores'),
    path('detalleEntrenador/<pk>', EntrenadorDetail.as_view(), name='DetalleEntrenador'),
    path('crearEntrenador/', EntrenadorCreate.as_view(), name='CrearEntrenador'),
    path('actualizarEntrenador/<pk>', EntrenadorUpdate.as_view(), name='ActualizarEntrenador'),
    path('eliminarEntrenador/<pk>', EntrenadorDelete.as_view(), name='EliminarEntrenador'),

    path('listaClientes/', ClienteList.as_view(), name='ListarClientes'),
    path('detalleCliente/<pk>', ClienteDetail.as_view(), name='DetalleCliente'),
    path('crearCliente/', ClienteCreate.as_view(), name='CrearCliente'),
    path('actualizarCliente/<pk>', ClienteUpdate.as_view(), name='ActualizarCliente'),
    path('eliminarCliente/<pk>', ClienteDelete.as_view(), name='EliminarCliente'),

    path('listaClases/', ClasesList.as_view(), name='ListarClases'),
    path('detalleClase/<pk>', ClasesDetail.as_view(), name='DetalleClase'),
    path('crearClase/', ClasesCreate.as_view(), name='CrearClase'),
    path('actualizarClase/<pk>', ClasesUpdate.as_view(), name='ActualizarClase'),
    path('eliminarClase/<pk>', ClasesDelete.as_view(), name='EliminarClase'),


    path('listaSedes/', SedesList.as_view(), name='ListarSedes'),
    path('detalleSede/<pk>', SedesDetail.as_view(), name='DetalleSede'),
    path('crearSede/', SedesCreate.as_view(), name='CrearSede'),
    path('actualizarSede/<pk>', SedesUpdate.as_view(), name='ActualizarSede'),
    path('eliminarSede/<pk>', SedesDelete.as_view(), name='EliminarSede')
]
