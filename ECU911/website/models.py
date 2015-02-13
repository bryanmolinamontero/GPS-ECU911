from django.db import models

# Create your models here.

class gps_lineas(models.Model):
    li_id  = models.AutoField(primary_key=True)
    li_numero_linea = models.CharField(max_length=25, blank=True)
    li_tipo = models.CharField(max_length=15, blank=True)
    li_ip = models.CharField(max_length=20, blank=True)
    li_fecha_solicitud = models.DateField(null=True, blank=True)
    li_fecha_activacion = models.DateField(null=True, blank=True)
    li_fecha_anulacion = models.DateField(null=True, blank=True)
    li_estado = models.CharField(max_length=15, blank=True)
    li_operadora = models.CharField(max_length=15, blank=True)
    li_servicio = models.CharField(max_length=25, blank=True)
    class Meta:
        db_table = 'gps_lineas'

    def __unicode__(self):
        return '%d, %s, %s, %s, %s, %s, %s, %s, %s, %s ' % (self.li_id, self.li_numero_linea, self.li_tipo,self.li_ip, self.li_fecha_solicitud, self.li_fecha_activacion, self.li_fecha_anulacion,self.li_estado, self.li_operadora, self.li_servicio)

class gps_sim_card (models.Model):
    si_id = models.AutoField(primary_key=True)
    si_simcard = models.CharField(max_length=25, blank=True)
    si_numero_linea = models.CharField(max_length=15, blank=True)
    si_fecha_inicio = models.DateField(null=True, blank=True)
    si_fecha_solicitud = models.DateField(null=True, blank=True)
    si_actual = models.BooleanField(blank=True)
    li_id = models.ForeignKey('gps_lineas', db_column='li_id')
    class Meta:
        db_table = 'gps_sim_card'

    def __unicode__(self):
        return '%d, %s, %s, %s, %s, %s, %s' % ( self.si_id, self.si_simcard, self.si_numero_linea, self.si_fecha_inicio, self.si_fecha_solicitud, self.si_actual, self.li_id)


class gps_imei(models.Model):
    im_id = models.AutoField(primary_key=True)
    im_imei = models.CharField(max_length=20, blank=True)
    im_serial = models.CharField(max_length=25, blank=True)
    im_codigo_gis = models.CharField(max_length=40, blank=True)
    im_estado = models.CharField(max_length=20, blank=True)
    im_origen = models.CharField(max_length=25, blank=True)
    im_lugar = models.CharField(max_length=50, blank=True)
    im_nota = models.CharField(max_length=350, blank=True)

    class Meta:
        db_table = 'gps_imei'

    def __unicode__(self):
        return '%d, %s, %s, %s, %s, %s, %s, %s' % (self.im_id, self.im_imei, self.im_serial, self.im_codigo_gis, self.im_estado, self.im_origen, self.lugar, self.im_nota)



class gps_instituciones(models.Model):
    in_id = models.AutoField(primary_key=True)
    in_nombre = models.CharField(max_length=150, blank=True)
    class Meta:
        db_table = 'gps_instituciones'

    def __unicode__(self):
        return '%d, %s' % (self.in_id, self.in_nombre)


class gps_tipo_unidades(models.Model):
    ti_id = models.AutoField(primary_key=True)
    ti_clase_unidad = models.CharField(max_length=150, blank=True)
    ti_nombre = models.CharField(max_length=150, blank=True)
    class Meta:
        db_table = 'gps_tipo_unidades'

    def __unicode__(self):
        return '%d, %s, %s' % (self.ti_id, self.ti_clase_unidad , self.ti_nombre)

class gps_departamento(models.Model):
    de_id = models.AutoField(primary_key=True)
    de_departmentId_gis = models.CharField(max_length=40, blank=True)
    de_departmentName = models.CharField(max_length=250, blank=True)
    de_EncargadoName = models.CharField(max_length=200, blank=True)
    de_departmentdireccion = models.CharField(max_length=250, blank=True)
    de_departmentPhone = models.CharField(max_length=15, blank=True)
    de_departmentFax = models.CharField(max_length=20, blank=True)
    de_departmentEmail = models.CharField(max_length=50, blank=True)
    de_notas = models.CharField(max_length=250, blank=True)

    class Meta:
        db_table = 'gps_departamento'

    def __unicode__(self):
        return '%d, %s, %s, %s, %s, %s, %s, %s, %s' % (self.de_id, self.de_departmentId_gis, self.de_departmentName, self.de_EncargadoName, self.de_departmentdireccion, self.de_departmentPhone, self.de_departmentFax, self.de_departmentEmail, self.de_notas)


class gps_cantones(models.Model):
    ca_id = models.AutoField(primary_key=True)
    ca_nombre = models.CharField(max_length=15, blank=True)
    ca_provincia = models.CharField(max_length=15, blank=True)

    class Meta:
        db_table = 'gps_cantones'

    def __unicode__(self):
        return '%d, %s, %s' % (self.ca_id, self.ca_nombre, self.ca_provincia)


'''class gps_unidades(models.Model):
    un_id = models.AutoField(primary_key=True)
    un_departamento = models.CharField(max_length=100, blank=True)
    un_ciudad = models.CharField(max_length=50, blank=True)--
    un_estado = models.CharField(max_length=50, blank=True)
    un_unidad = models.CharField(max_length=100, blank=True)
    un_codigo_gis = models.CharField(max_length=100, blank=True)
    un_persona = models.CharField(max_length=50, blank=True)
    un_telefono = models.CharField(max_length=50, blank=True)
    un_notas = models.CharField(max_length=250, blank=True)
    un_placa = models.CharField(max_length=50, blank=True)
    un_modelo = models.CharField(max_length=100, blank=True)
    un_uso = models.CharField(max_length=250, blank=True)
    un_asignado_sistema = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'gps_unidades'

    def __unicode__(self):
        return '%d, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s' % (self.un_id, self.un_institucion, self.un_departamento, self.un_ciudad, self.un_tipo, self.un_estado, self.un_unidad, self.un_codigo_gis, self.un_persona, self.un_telefono, self.un_notas, self.un_placa, self.un_modelo, self.un_uso, self.un_asignado_sistema)
'''