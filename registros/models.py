from django.db import models
from simple_history.models import HistoricalRecords
from django.urls import reverse
from usuarios.models import Perfil


class Incluido(models.Model):
    sino = (('1', 'Sí'), ('2', 'No'))
    provincia = models.TextField(blank=True, null=True)
    municipio = models.TextField(blank=True, null=True)
    sclinico = models.TextField(blank=True, null=True)
    numero = models.IntegerField("No.")
    iniciales = models.CharField("Iniciales del sujeto", max_length=10)
    feceva = models.DateField("Fecha de evaluación")
    inclusion = models.CharField("¿El sujeto se incluyo?", max_length=2, choices=sino)
    fecinc = models.DateField("Fecha de Inclusión", null=True, blank=True)
    codigo = models.CharField("Codigo del sujeto", max_length=11, null=True, blank=True)
    causano = models.IntegerField("Si no incluido refiera número de causa")
    investigador = models.CharField("Investigador", max_length=100)
    firma = models.CharField("Firma", max_length=2, choices=sino)
    history = HistoricalRecords()

    def save(self, *args, **kwargs):
        self.provincia = Perfil.history.values()[0]['provincia']
        self.municipio = Perfil.history.values()[0]['municipio']
        self.sclinico = Perfil.history.values()[0]['sclinico']
        super(Incluido, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('inc_detail', kwargs={'pk': self.pk})


class RecDevPi(models.Model):
    fecha = models.DateField("Fecha")
    cantidad_1 = models.IntegerField("Cantidad de bolsas individuales")
    codigo_1 = models.TextField("Código de las bolsas")
    entrega_1 = models.CharField("Entrega", max_length=100)
    recibe_1 = models.CharField("Recibe", max_length=100)
    cantidad_2 = models.IntegerField("Cantidad de bolsas individuales utilizadas")
    cantidad_3 = models.IntegerField("Cantidad de bolsas individuales sin utilizar")
    codigo_2 = models.TextField("Código de las bolsas sin utilizar")
    entrega_2 = models.CharField("Entrega", max_length=100)
    recibe_2 = models.CharField("Recibe", max_length=100)
    history = HistoricalRecords()

    def get_absolute_url(self):
        return reverse('rdpi_detail', kwargs={'pk': self.pk})
