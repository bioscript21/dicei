from django.db import models
from simple_history.models import HistoricalRecords
from django.urls import reverse


class Incluido(models.Model):
    sino = (('1', 'Sí'), ('2', 'No'))
    numero = models.IntegerField()
    iniciales = models.CharField(max_length=10)
    feceva = models.DateField()
    inclusion = models.CharField(max_length=2, choices=sino)
    fecinc = models.DateField(null=True, blank=True)
    numinc = models.IntegerField(null=True, blank=True)
    causano = models.IntegerField()
    investigador = models.CharField(max_length=100)
    firma = models.CharField(max_length=2, choices=sino)
    history = HistoricalRecords()

    def get_absolute_url(self):
        return reverse('inc_detail', kwargs={'pk': self.pk})
