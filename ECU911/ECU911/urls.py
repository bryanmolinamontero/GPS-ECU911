from django.conf.urls import patterns, include, url
from website.views import *
from ECU911 import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ECU911.views.home', name='home'),
    # url(r'^ECU911/', include('ECU911.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,}),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', index),
    url(r'^index/$', index),


    #LINEAS
    #****************************
    url(r'^lineas/$', lineas),
    url(r'^ingresarLinea/$', ingresarLinea),
    url(r'^submitIngresarLinea/$', submitIngresarLinea),
    url(r'^ingresarLinea/$', ingresarLinea),
    url(r'^editarLinea/$', editarLinea),
    url(r'^anularLinea/$', anularLinea),

        #************** VALIDACIONES
        url(r'^validarIP/$', validarIP ),
        url(r'^validarNumero/$', validarNumero ),
        url(r'^validarSim_card/$', validarSim_card ),

    #****************************


    #GPS
    #****************************
    url(r'^gps/$', gps),
    url(r'^editarGPS/$', editarGPS),
    url(r'^ingresarGPS/$', ingresarGPS),
    url(r'^submitGPS/$', submitGPS),
    url(r'^eliminarGPS/$', eliminarGPS),

    #****************************

    #UNIDADES
    #*****************************
    url(r'^unidades/$', unidades),
    url(r'^ingresarUnidad/$', ingresarUnidad),
    url(r'^submitIngresarUnidad/$', submitIngresarUnidad),
    url(r'^cargarComboBoxInstituciones/$', cargarComboBoxInstituciones),
    url(r'^cargarComboBoxDepartamentos/$', cargarComboBoxDepartamentos),
    url(r'^cargarComboBoxCiudades/$', cargarComboBoxCiudades),
    url(r'^cargarComboBoxTipoDeUnidad/$', cargarComboBoxTipoDeUnidad),
    url(r'^editarUnidad/$', editarUnidad),
    url(r'^anularUnidad/$', anularUnidad),

    #url(r'^editarUnidad/$', editarUnidad),
    #*****************************

    #SIMCARD
    #*****************************
    #url(r'^historialSimCard/$', historialSimCard),
    url(r'^cambiarSimCard/(?P<numeroLinea>\w+)/$',cambiarSimCard),
    url(r'^submitCambiarSimCard/$',submitCambiarSimCard),
    url(r'^historialSimCard/(?P<idSimCard>\d+)/$',historialSimCard),
    #*****************************


    #ACTAS
    #********************************
    url(r'^ingresarActa/$', ingresarActa),
    url(r'^submitIngresarActa/$', submitIngresarActa),
    url(r'^ingresarImagen/$', ingresarImagen),
    url(r'^buscarDepartamentoPorInstitucion/$', buscarDepartamentoPorInstitucion),

    url(r'^visualizarActa/$', visualizarActa),
        url(r'^consultarActa/(?P<id_uli>\d+)/$',consultarActa),



    #************* VALIDACIONES
    url(r'^verificarUnidad/$', verificarUnidad),
    url(r'^verificarImei/$', verificarImei),
    url(r'^verificarNroTarjetaSim/$', verificarNroTarjetaSim),

)
