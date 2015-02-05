# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response

from models import *


def index(request):
    return render_to_response('index.html')




#LINEAS
#*************************************************************************

def lineas(request):
    registros = gps_lineas.objects.all()
    return render_to_response('lineas.html', {"registros":registros})


def ingresarLinea(request):
    return render_to_response('ingresarLinea.html')
#*************************************************************************



#GPS
#***************************************************************************
def gps(request):
    registrosGPS = gps_imei.objects.all().order_by("im_id")
    return render_to_response('gps.html', {"registros":registrosGPS})


def editarGPS(request):
    if request.POST:

        id=request.POST['id']
        imei=request.POST['imei']
        serial=request.POST['serial']
        gis=request.POST['gis']
        estado=request.POST['estado']
        origen=request.POST['origen']
        lugar=request.POST['lugar']
        nota=request.POST['nota']
        editarRegistro = gps_imei(im_id=id, im_imei=imei, im_serial=serial, im_codigo_gis=gis, im_estado=estado, im_origen=origen, im_lugar=lugar, im_nota=nota)
        editarRegistro.save()

        return HttpResponseRedirect('/gps/')
    else:
        return HttpResponseRedirect('/')



def ingresarGPS(request):
    return render_to_response('ingresarGPS.html')

def submitGPS(request):
    if request.POST:

        imei=request.POST['imei']
        serial=request.POST['serial']
        gis=request.POST['gis']
        estado=request.POST['estado']
        origen=request.POST['origen']
        lugar=request.POST['lugar']
        nota=request.POST['nota']
        guardarRegistro = gps_imei(im_imei=imei, im_serial=serial, im_codigo_gis=gis, im_estado=estado, im_origen=origen, im_lugar=lugar, im_nota=nota)
        guardarRegistro.save()

        return HttpResponseRedirect('/gps/')
    else:
        return HttpResponseRedirect('/gps/')


def eliminarGPS(request):
    if request.GET:
        try:
            id =  request.GET['id']
            eliminar = gps_imei.objects.get(im_id=id)
            eliminar.delete()
            return HttpResponse("Registro Eliminado")
        except Exception as ex:
            return HttpResponse("No se pudo eliminar")
    else:
        return HttpResponseRedirect('/gps/')

#***************************************************************************



#UNIDADES
#***************************************************************************
def unidades(request):
    registrosUnidades = gps_unidades.objects.all().order_by("un_id")
    return render_to_response('unidades.html', {"registros":registrosUnidades})
#***************************************************************************

