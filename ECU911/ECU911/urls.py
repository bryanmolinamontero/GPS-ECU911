from django.conf.urls import patterns, include, url
from website.views import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ECU911.views.home', name='home'),
    # url(r'^ECU911/', include('ECU911.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', index),
    url(r'^index/$', index),
    url(r'^lineas/$', lineas),


    #GPS
    #****************************
    url(r'^gps/$', gps),
    url(r'^editarGPS/$', editarGPS),
    url(r'^ingresarGPS/$', ingresarGPS),
    url(r'^submitGPS/$', submitGPS),
    #****************************

    #UNIDADES
    #*****************************
    url(r'^unidades/$', unidades),
    #*****************************


)
