# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response

from models import *


def index(request):
    return render_to_response('index.html')




#LINEAS
#*************************************************************************

def lineas(request):
    registros = gps_lineas.objects.all().order_by("-li_id")
    return render_to_response('lineas.html', {"registros":registros})


def ingresarLinea(request):
    return render_to_response('ingresarLinea.html')

def submitIngresarLinea(request):
    if request.POST:
        operadora=request.POST['operadora']
        tipo_plan = request.POST['radio1']
        otro_tipo = request.POST['otro_tipo']
        ip = request.POST['ip']
        numero = request.POST['numero']
        fecha_activacion = request.POST['fecha_activacion']
        fecha_solicitud = request.POST['fecha_solicitud']
        fecha_anulacion = request.POST['fecha_anulacion']
        tipo_servicio = request.POST['radio2']
        otro_servicio = request.POST['otro_servicio']
        sim_card = request.POST['sim_card']
        tipo_planFinal = ""
        tipo_servicioFinal = ""
        if otro_tipo == "":
            tipo_planFinal=tipo_plan
        else:
            tipo_planFinal = otro_tipo

        if otro_servicio =="":
            tipo_servicioFinal=tipo_servicio
        else:
            tipo_servicioFinal = otro_servicio
        #self.li_id, self.li_numero_linea, self.li_tipo,self.li_ip, self.li_fecha_solicitud, self.li_fecha_activacion, self.li_fecha_anulacion,self.li_estado, self.li_operadora, self.li_servicio)
        guardarRegistroLineas = gps_lineas(li_numero_linea = numero , li_tipo = tipo_planFinal , li_ip = ip, li_fecha_solicitud = fecha_solicitud , li_fecha_activacion = fecha_activacion, li_estado = "ACTIVA", li_operadora = operadora, li_servicio = tipo_servicioFinal)
        guardarRegistroLineas.save()


        #DATOS QUE  SE GUARDAN EN LA TABLA GPS_SIM_CARD
        obtenerId = gps_lineas.objects.get(li_numero_linea = numero)
        guardarRegistroSimCard = gps_sim_card(si_simcard = sim_card , si_numero_linea = numero , si_fecha_inicio = fecha_activacion , si_fecha_solicitud = fecha_solicitud, si_actual = True ,  li_id = obtenerId)
        guardarRegistroSimCard.save()
        #self.si_id, self.si_simcard, self.si_numero_linea, self.si_fecha_inicio, self.si_fecha_solicitud, self.si_actual, self.li_id)


        return HttpResponseRedirect('/lineas/')
        #return HttpResponse(operadora + " - " + tipo_planFinal + " - " + ip + " - " + numero + " - " + fecha_activacion + " - " + fecha_solicitud + " - " + fecha_anulacion + " - " + tipo_servicioFinal + " - " +  sim_card)

    else:
        return HttpResponseRedirect('/lineas/')

def anularLinea(request):
    if request.POST:
        id=request.POST['id']
        fecha_anulacion=request.POST['fecha_anulacion2']

        print "**************"
        print id
        print fecha_anulacion
        print "**************"
        anularRegistro = gps_lineas.objects.filter(li_id=id).update(li_fecha_anulacion = fecha_anulacion, li_estado="ANULADA")
        return HttpResponseRedirect('/lineas/')
    else:
        return HttpResponseRedirect('/lineas/')

def editarLinea(request):
    if request.POST:
        id = request.POST['id']
        operadora=request.POST['operadora']
        tipo_plan = request.POST['radio1']
        otro_tipo = request.POST['otro_tipo']
        ip = request.POST['ip']
        numero = request.POST['numero']
        fecha_activacion = request.POST['fecha_activacion']
        fecha_solicitud = request.POST['fecha_solicitud']
        fecha_anulacion = request.POST['fecha_anulacion']
        tipo_servicio = request.POST['radio2']
        otro_servicio = request.POST['otro_servicio']
        #sim_card = request.POST['sim_card']
        tipo_planFinal = ""
        tipo_servicioFinal = ""
        if otro_tipo == "":
            tipo_planFinal=tipo_plan
        else:
            tipo_planFinal = otro_tipo

        if otro_servicio =="":
            tipo_servicioFinal=tipo_servicio
        else:
            tipo_servicioFinal = otro_servicio

        '''print "*********************"
        print id #no se modificada
        print operadora
        print tipo_planFinal
        print ip
        print numero #tampoco no se modfica
        print fecha_activacion
        print fecha_solicitud
        print fecha_anulacion
        print tipo_servicioFinal
        print "*********************"'''
        gps_lineas.objects.filter(li_id = id).update(li_tipo = tipo_planFinal, li_ip = ip , li_fecha_solicitud = fecha_solicitud, li_fecha_activacion = fecha_activacion , li_fecha_anulacion = fecha_anulacion , li_operadora = operadora, li_servicio = tipo_servicioFinal)
        return HttpResponseRedirect('/lineas/')
    else:
        return HttpResponseRedirect('/lineas/')


    #********************** VALIDACIONES
def validarIP(request):
        if request.GET:
            try:
                ip =  request.GET['ip']
                verificarIP = gps_lineas.objects.filter(li_ip=ip)
                cont = 0
                for i in verificarIP:
                    cont  = cont +1

                if cont>0:
                    return HttpResponse("False")
                else:
                    return HttpResponse("True")

            except Exception as ex:
                return "ERROR"
        else:
            return HttpResponseRedirect('/lineas/')


def validarNumero(request):
        if request.GET:
            try:
                numero =  request.GET['numero']
                verificarNumero = gps_lineas.objects.filter(li_numero_linea = numero)
                cont = 0
                for i in verificarNumero:
                    cont  = cont +1

                if cont>0:
                    return HttpResponse("False")
                else:
                    return HttpResponse("True")

            except Exception as ex:
                return "ERROR"
        else:
            return HttpResponseRedirect('/lineas/')

def validarSim_card(request):
        if request.GET:
            try:
                sim_card =  request.GET['sim_card']
                verificarSim_card = gps_sim_card.objects.filter(si_simcard = sim_card)
                #verificarSim_card = gps_lineas.objects.filter(li_numero_linea = sim_card)
                cont = 0
                for i in verificarSim_card:
                    cont  = cont +1

                if cont>0:
                    return HttpResponse("False")
                else:
                    return HttpResponse("True")

            except Exception as ex:
                return "ERROR"
        else:
            return HttpResponseRedirect('/lineas/')



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

def ingresarUnidad(request):
    return render_to_response('ingresarUnidad.html')

#***************************************************************************


#HISTORIAL SIM CARD
def historialSimCard(request, idSimCard):
    registrosSimCard = gps_sim_card.objects.filter(li_id=idSimCard)
    return render_to_response('historialSimCard.html', {"registros":registrosSimCard})

def cambiarSimCard(request, numeroLinea):
    registrodeLinea = gps_lineas.objects.filter(li_numero_linea=numeroLinea)
    cont = 0
    for i in registrodeLinea:
        cont = cont + 1
    if cont>0:
        return render_to_response('cambiarSimCard.html', {"linea":numeroLinea})
    else:
        return HttpResponseRedirect('/lineas/')


def submitCambiarSimCard(request):
    if request.POST:
        linea = request.POST['linea']
        sim_card = request.POST['sim_card']
        fecha_inicio = request.POST['fecha_inicio']
        fecha_solicitud = request.POST['fecha_solicitud']
        estado="False"

        try:
            estado = request.POST['estado']
        except:
                False

        if estado=="False":
            estado = False
        else:
            estado = True
            gps_sim_card.objects.filter(si_numero_linea = linea).update(si_actual = False)


        obtenerId = gps_lineas.objects.get(li_numero_linea = linea)
        guardarRegistroGpsSimCard = gps_sim_card(si_simcard = sim_card ,si_numero_linea = linea  ,si_fecha_inicio = fecha_inicio, si_fecha_solicitud = fecha_solicitud, si_actual = estado, li_id = obtenerId)
        guardarRegistroGpsSimCard.save()

        return HttpResponseRedirect('/lineas/')

    else:
        return HttpResponseRedirect('/lineas/')

