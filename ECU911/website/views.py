# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.db import transaction
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
    registrosInstituciones = gps_instituciones.objects.all().order_by("in_id")
    registrosDepartamentos = gps_departamento.objects.all().order_by("de_id")
    registrosCantones = gps_cantones.objects.all().order_by("ca_id")
    registrosTipo = gps_tipo_unidades.objects.all().order_by("ti_id")
    return render_to_response('ingresarUnidad.html' , {"registrosInstituciones": registrosInstituciones, "registrosDepartamentos":registrosDepartamentos, "registrosCantones":registrosCantones , "registrosTipo":registrosTipo})

def submitIngresarUnidad(request):
    if request.POST:
        #----- FORANEAS-----
        institucion = request.POST['instituciones']
        departamento = request.POST['departamentos']
        ciudad = request.POST['ciudades']
        tipo = request.POST['tipo']
        #------------------
        estado = request.POST['estado']
        unidad = request.POST['unidad']  #es el nombre
        persona = request.POST['persona']
        telefono = request.POST['telefono']
        placa = request.POST['placa']
        modelo = request.POST['modelo']
        uso = request.POST['uso']
        notas = request.POST['notas']
        codigo_gis = request.POST['codigo_gis']
        asignado_sistema = request.POST['asignado_sistema']

        marca =  request.POST['marca']
        anio =  request.POST['anio']
        #----- FORANEAS-----
        '''print institucion
        print departamento
        print ciudad
        print tipo'''
        foraneaInstitucion = gps_instituciones.objects.get(in_id = institucion)
        foraneaDepartamento = gps_departamento.objects.get(de_id = departamento)
        foraneaCiudad = gps_cantones.objects.get(ca_id = ciudad)
        foraneaTipo = gps_tipo_unidades.objects.get(ti_id = tipo)
        #------------------
        '''print estado
        print unidad
        print persona
        print placa
        print modelo
        print uso
        print codigo_gis
        print asignado_sistema'''
        guardarUnidad = gps_unidades(un_estado = estado, un_unidad = unidad, un_codigo_gis = codigo_gis, un_persona =  persona , un_telefono = telefono, un_notas = notas, un_placa = placa, un_modelo = modelo, un_uso = uso, un_asignado_sistema = asignado_sistema, un_institucion_id = foraneaInstitucion, un_departamento_id = foraneaDepartamento, un_canton_id = foraneaCiudad, un_tipounidad_id = foraneaTipo , un_marca= marca, un_anio=anio)
        guardarUnidad.save()
        return HttpResponseRedirect('/unidades/')
    else:
        return HttpResponseRedirect('/unidades/')

def ingresarUnidad(request):
    registrosInstituciones = gps_instituciones.objects.all().order_by("in_id")
    registrosDepartamentos = gps_departamento.objects.all().order_by("de_id")
    registrosCantones = gps_cantones.objects.all().order_by("ca_id")
    registrosTipo = gps_tipo_unidades.objects.all().order_by("ti_id")
    return render_to_response('ingresarUnidad.html' , {"registrosInstituciones": registrosInstituciones, "registrosDepartamentos":registrosDepartamentos, "registrosCantones":registrosCantones , "registrosTipo":registrosTipo})

from django.core import serializers
from django.http import HttpResponse
def cargarComboBoxInstituciones(request):
    registrosInstituciones = gps_instituciones.objects.all().order_by("in_id")
    data = serializers.serialize('json', registrosInstituciones, fields=('in_id','in_nombre'))
    return HttpResponse(data, mimetype='application/json')

def cargarComboBoxDepartamentos(request):
    registrosDepartamentos = gps_departamento.objects.all().order_by("de_id")
    data = serializers.serialize('json', registrosDepartamentos, fields=('de_id','de_departmentName'))
    return HttpResponse(data, mimetype='application/json')

def cargarComboBoxCiudades(request):
    registrosCantones = gps_cantones.objects.all().order_by("ca_id")
    data = serializers.serialize('json', registrosCantones, fields=('ca_id','ca_nombre'))
    return HttpResponse(data, mimetype='application/json')

def cargarComboBoxTipoDeUnidad(request):
    registrosTipoDeUnidad = gps_tipo_unidades.objects.all().order_by("ti_id")
    data = serializers.serialize('json', registrosTipoDeUnidad, fields=('ti_id','ti_nombre'))
    return HttpResponse(data, mimetype='application/json')


def editarUnidad(request):
    if request.POST:
        #----- FORANEAS-----
        institucion = request.POST['instituciones']
        departamento = request.POST['departamentos']
        ciudad = request.POST['ciudades']
        tipo = request.POST['tipo']
        #------------------
        id = request.POST['id']
        estado = request.POST['estado']
        unidad = request.POST['unidad']  #es el nombre
        persona = request.POST['persona']
        telefono = request.POST['telefono']
        placa = request.POST['placa']
        modelo = request.POST['modelo']
        uso = request.POST['uso']
        notas = request.POST['notas']
        codigo_gis = request.POST['codigo_gis']
        asignado_sistema = request.POST['asignado_sistema']

        marca =  request.POST['marca']
        anio =  request.POST['anio']

        #----- FORANEAS-----
        print institucion
        print departamento
        print ciudad
        print tipo
        foraneaInstitucion = gps_instituciones.objects.get(in_id = institucion)
        foraneaDepartamento = gps_departamento.objects.get(de_id = departamento)
        foraneaCiudad = gps_cantones.objects.get(ca_id = ciudad)
        foraneaTipo = gps_tipo_unidades.objects.get(ti_id = tipo)
        #------------------
        print estado
        print unidad
        print persona
        print telefono
        print placa
        print modelo
        print uso
        print notas
        print codigo_gis
        print asignado_sistema
        gps_unidades.objects.filter(un_id = id).update(un_estado = estado, un_unidad = unidad, un_codigo_gis = codigo_gis, un_persona =  persona , un_telefono = telefono, un_notas = notas, un_placa = placa, un_modelo = modelo, un_uso = uso, un_asignado_sistema = asignado_sistema, un_institucion_id = foraneaInstitucion, un_departamento_id = foraneaDepartamento, un_canton_id = foraneaCiudad, un_tipounidad_id = foraneaTipo , un_marca=marca , un_anio=anio)
        #gps_unidades.objects.filter(li_id = id).update(li_tipo = tipo_planFinal, li_ip = ip , li_fecha_solicitud = fecha_solicitud, li_fecha_activacion = fecha_activacion , li_fecha_anulacion = fecha_anulacion , li_operadora = operadora, li_servicio = tipo_servicioFinal)
        return HttpResponseRedirect('/unidades/')
    else:
        return HttpResponseRedirect('/unidades/')

def anularUnidad(request):
        if request.POST:
            id = request.POST['id2']
            gps_unidades.objects.filter(un_id = id).update(un_estado="NO DISPONIBLE")
            print id
            return HttpResponseRedirect('/unidades/')
        else:
            return HttpResponseRedirect('/unidades/')

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


#*************** ACTAS ************




def ingresarActa(request):
    registrosInstituciones = gps_instituciones.objects.all().order_by("in_id")
    registrosCantones = gps_cantones.objects.all().order_by("ca_id")
    registrosUnidades = gps_unidades.objects.all().order_by("un_id")
    registrosGPS = gps_imei.objects.all().order_by("im_id")
    registrosTipoUnidades = gps_tipo_unidades.objects.all().order_by("ti_id")
    #vista para el combo no tarjeta sim
    from django.db import connection
    cursor = connection.cursor()
    sql = 'select gps_lineas.li_id, li_numero_linea, si_id, si_simcard, si_actual from gps_lineas, gps_sim_card where gps_lineas.li_id = gps_sim_card.li_id and si_actual=TRUE'
    cursor.execute(sql)
    registrosNTarjetaSim = cursor.fetchall()

    return  render_to_response('ingresarActa.html', {"registrosInstituciones":registrosInstituciones, "registrosCantones":registrosCantones, "registrosUnidades":registrosUnidades, "registrosGps":registrosGPS, "registrosTipoUnidades":registrosTipoUnidades, "registrosNTarjetaSim":registrosNTarjetaSim})

@transaction.commit_manually
def submitIngresarActa(request):
    if request.POST:
        institucion = request.POST['institucion']
        departamento = request.POST['departamentos']
        provincia = request.POST['provinciaDeTrabajo']
        ciudad = request.POST['ciudades'] #es el CANTON
        lugarDeInstalacion = request.POST['lugarDeInstalacion']
        fechaDeInstalacion = request.POST['fechaDeInstalacion'] # solo date
        fechaDeCreacion = request.POST['fechaDeCreacion'] #datetime
        nombreUnidad = request.POST['nombreUnidad']
        codigoUnidad = request.POST['codigoUnidad']
        marcaVehiculo = request.POST['marcaVehiculo']
        modeloVehiculo = request.POST['modeloVehiculo']
        placaVehiculo = request.POST['placaVehiculo']
        anioVehiculo = request.POST['anioVehiculo']
        estadoVehiculo = request.POST['estadoVehiculo']
        puntoDeInstalacion = request.POST['puntoDeInstalacion']
        codigoImei = request.POST['codigoImei']
        imei = request.POST['imei']
        numeroDeSerie = request.POST['numeroDeSerie']
        nombreDeServidor = request.POST['nombreDeServidor']
        IDnroTarjeta = request.POST['IDnroTarjeta']
        nroTarjeta = request.POST['nroTarjeta'] #es la LINEA
        IDSimCard = request.POST['IDSimCard']
        nroSerialTarjetaSim = request.POST['nroSerialTarjetaSim']
        contrasenia =  request.POST['contrasenia']
        intervaloTransmision = request.POST['intervaloTransmision']
        voltaje = request.POST['voltaje']
        tipoVehiculo = request.POST['tipoVehiculo']
        nota = request.POST['nota']

        imagen1 = None
        imagen2 = None

        try:
            imagen1 = request.FILES['imagen1']
        except Exception as ex:
            print "No se ha ingresado imagen 1"
        try:
            imagen2 = request.FILES['imagen2']
        except Exception as ex:
            print "No se ha ingresado imagen 2"

        #*** dos paneles de abajo***
        nombreInstalador = request.POST['nombreInstalador']
        cargoInstalador = request.POST['cargoInstalador']
        nombreResponsable = request.POST['nombreResponsable']
        cargoResponsable = request.POST['cargoResponsable']

        #***************************

        idLinea = gps_lineas.objects.get(li_id=IDnroTarjeta)
        idImei = gps_imei.objects.get(im_id=codigoImei)
        idUnidad =gps_unidades.objects.get(un_id=codigoUnidad)
        idGpsSimCard = gps_sim_card.objects.get(si_id=IDSimCard)
        idDepartamento = gps_departamento.objects.get(de_id=departamento)

        try:
            registroULI = gps_imei_linea_unidad(uli_imei=imei, uli_linea=nroTarjeta, uli_canton = ciudad, uli_unidad = nombreUnidad, uli_estado_unidad =estadoVehiculo, uli_fecha_inicio = fechaDeInstalacion, uli_estado_actual="ACTIVO",  uli_fecha_creacion=fechaDeCreacion, uli_fecha_modificacion=fechaDeCreacion, uli_estado_registro = True, uli_linea_id=idLinea, uli_imei_id = idImei, uli_unidades_id = idUnidad, uli_sim_card_id= idGpsSimCard, uli_departamento_id = idDepartamento)
            registroULI.save()
            extraerInstitucion = gps_instituciones.objects.get(in_id=institucion)
            idUli = gps_imei_linea_unidad.objects.get(uli_imei=imei, uli_linea=nroTarjeta, uli_canton = ciudad, uli_unidad = nombreUnidad,uli_estado_unidad =estadoVehiculo, uli_fecha_inicio = fechaDeInstalacion)
            registroActas = gps_actas(ac_tipo = "", ac_fecha_instalacion = fechaDeInstalacion, ac_punto_instalacion = puntoDeInstalacion, ac_nombre_servidor = nombreDeServidor, ac_contrasenia = contrasenia, ac_intervalo = intervaloTransmision, ac_voltaje = voltaje, ac_nota = nota, ac_lugar_de_instalacion = lugarDeInstalacion, ac_canton = ciudad, ac_provincia = provincia, ac_imei = imei, ac_serie_imei= numeroDeSerie, ac_linea= nroTarjeta, ac_sim_card= nroSerialTarjetaSim, ac_unidad = nombreUnidad, ac_institucion= extraerInstitucion.in_nombre, ac_departamento = idDepartamento.de_departmentName, ac_marca_unidad= marcaVehiculo, ac_modelo_unidad= modeloVehiculo, ac_placa_unidad= placaVehiculo, ac_anio_unidad= anioVehiculo, ac_estado_unidad = estadoVehiculo, ac_tipo_vehiculo = tipoVehiculo,  ac_tecnico = nombreInstalador, ac_cargo_tecnico = cargoInstalador, ac_responsable_unidad = nombreResponsable, ac_cargo_responsable = cargoResponsable, ac_estado_registro = True, ac_uli_id = idUli , ac_imagen1 =  imagen1, ac_imagen2 = imagen2)
            registroActas.save()
            transaction.commit()

            return render_to_response('mensajes.html', {"mensaje":"Acta Guardada Correctamente... Redireccionando, por favor espere...", "pagina":"/ingresarActa/"})
        except:
            transaction.rollback()
            return render_to_response('mensajes.html', {"mensaje":"Ha ocurrido un error...", "pagina":"/ingresarActa/"})
    else:
        return HttpResponseRedirect('/ingresarActa/')


def visualizarActa(request):
    registros_imei_linea_unidad = gps_imei_linea_unidad.objects.all()

    return render_to_response('visualizarActa.html', {"registros_imei_linea_unidad":registros_imei_linea_unidad})

def consultarActa(request, id_uli):

    id = id_uli
    registro_uli = gps_imei_linea_unidad.objects.get(uli_id=id)
    registro_acta = gps_actas.objects.get(ac_uli_id=registro_uli.uli_id)

    return render_to_response('consultarActa.html', {"registro_acta":registro_acta})
#    return HttpResponse(registro_acta)

#**********************************


def ingresarImagen(request):

    imagen = request.FILES['imagen1']
    print "*********************"
    print "*****m****************"
    print imagen
    print "*********************"
    print "*********************"
    registro = pruebita(imagen= imagen)
    registro.save()
    return HttpResponse("sda")



def ingresarActa2(req):
    #select gps_lineas.li_id, li_numero_linea, si_simcard, si_actual from gps_lineas, gps_sim_card
    #where gps_lineas.li_id = gps_sim_card.li_id and si_actual=TRUE
    #registros = gps_lineas.objects
    from django.db import connection
    cursor = connection.cursor()
    sql = 'select gps_lineas.li_id, li_numero_linea, si_id, si_simcard, si_actual from gps_lineas, gps_sim_card where gps_lineas.li_id = gps_sim_card.li_id and si_actual=TRUE'
    cursor.execute(sql)
    results = cursor.fetchall()
    return render_to_response('pr.html',{"lst":results})


from django.core import serializers
def buscarDepartamentoPorInstitucion(request):
    if request.GET:
        id=request.GET['id']
        departamentos= gps_departamento.objects.filter(de_id_institucion=id)
        data = serializers.serialize('json', departamentos,fields=('de_departmentName'))
        return HttpResponse(data, mimetype='application/json')
    else:
        return HttpResponseRedirect("/ingresarUnidad/")



def verificarUnidad(request):
    if request.GET:
        print "*****************"
        print "*****************"
        print "*****************"
        id=request.GET['id']#select * from gps_imei_linea_unidad where un_id=9 and  uli_estado_actual='ACTIVO'
        print "1"
        unidades= gps_imei_linea_unidad.objects.filter(uli_unidades_id=id, uli_estado_actual='ACTIVO')
        print "2"
        cont = 0
        print "3"
        for i in unidades:
            cont = cont + 1
        print "4"
        if cont == 0:
            print "5"
            return HttpResponse("FALSE") #CUANDO NO HAY REGISTROS EN ESE SELECT Y SI LO PUEDE ESCOGER
        else:
            print "6"
            return HttpResponse("TRUE") #CUANDO SI HAY REGISTROS EN ESE SELECT Y NO LO PUEDE ESCOGER
    else:
        return HttpResponseRedirect("/ingresarActa/")

def verificarImei(request):
    if request.GET:
        id=request.GET['id']#select * from gps_imei_linea_unidad where un_id=9 and  uli_estado_actual='ACTIVO'
        imeis= gps_imei_linea_unidad.objects.filter(uli_imei_id=id, uli_estado_actual='ACTIVO')
        cont = 0
        for i in imeis:
            cont = cont + 1
        if cont == 0:
            return HttpResponse("FALSE") #CUANDO NO HAY REGISTROS EN ESE SELECT Y SI LO PUEDE ESCOGER
        else:
            return HttpResponse("TRUE") #CUANDO SI HAY REGISTROS EN ESE SELECT Y NO LO PUEDE ESCOGER
    else:
        return HttpResponseRedirect("/ingresarActa/")

def verificarNroTarjetaSim(request):
    if request.GET:
        id=request.GET['id']#select * from gps_imei_linea_unidad where un_id=9 and  uli_estado_actual='ACTIVO'
        lineas= gps_imei_linea_unidad.objects.filter(uli_linea_id=id, uli_estado_actual='ACTIVO')
        cont = 0
        for i in lineas:
            cont = cont + 1
        if cont == 0:
            return HttpResponse("FALSE") #CUANDO NO HAY REGISTROS EN ESE SELECT Y SI LO PUEDE ESCOGER
        else:
            return HttpResponse("TRUE") #CUANDO SI HAY REGISTROS EN ESE SELECT Y NO LO PUEDE ESCOGER
    else:
        return HttpResponseRedirect("/ingresarActa/")