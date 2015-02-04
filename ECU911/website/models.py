from django.db import models

# Create your models here.

class gps_lineas(models.Model):
    li_id  = models.AutoField(primary_key=True)
    li_estado = models.CharField(max_length=10, blank=True)
    li_numero = models.CharField(max_length=20, blank=True)
    li_tipo = models.CharField(max_length=15, blank=True)
    li_ip = models.CharField(max_length=15, blank=True)
    li_fecha_activacion = models.DateField(null=True, blank=True)
    li_fecha_anulacion = models.DateField(null=True, blank=True) # Field renamed to remove unsuitable characters.
    class Meta:
        db_table = 'gps_lineas'

    def __unicode__(self):
        return '%d, %s, %s, %s, %s, %s, %s ' % (self.li_id, self.li_estado, self.li_numero, self.li_tipo, self.li_ip, self.li_fecha_activacion, self.li_fecha_anulacion)


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


class gps_unidades(models.Model):
    un_id = models.AutoField(primary_key=True)
    un_institucion = models.CharField(max_length=50, blank=True)
    un_departamento = models.CharField(max_length=100, blank=True)
    un_ciudad = models.CharField(max_length=50, blank=True)
    un_tipo = models.CharField(max_length=50, blank=True)
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
