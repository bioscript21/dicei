from django.db import models
from simple_history.models import HistoricalRecords
from simple_history import register
from django.contrib.auth.models import User
from PIL import Image

register(User)


class Perfil(models.Model):
    cprov = (('LH', 'La Habana'), ('CIE', 'Cienfuegos'), ('VC', 'Villa Clara'), ('SC', 'Santiago de cuba'))

    cmunic = (('SA', 'Santa Clara'), ('CA', 'Camajuaní'), ('RE', 'Remedios'), ('CI', 'Caibarien'),
              ('SC', 'Santiago de Cuba'))

    csitio = (('IN', 'Infanti Norte'), ('IS', 'Infantil Sur'), ('CJ', 'Pol. Carlos J Finlay'),
              ('CT', 'Pol. Camilo Torres'), ('LP', 'Pol. López Peña'), ('28', 'Pol. 28 de Septiembre'),
              ('30', 'Pol 30 de Noviembre'), ('JJ', 'Pol. José Martí'), ('JP', 'Pol. Josué País'), ('LS', 'CPHEM SC'),
              ('ES', 'EMCOMED Santiago de Cuba'), ('LO', 'Laboratorio Oriente'), ('LF', 'Lab. Inmunología Clínica IFV'),
              ('JL', 'HPP José Luis Miranda'), ('SA', 'Pol. Santa Clara'), ('JR', 'Pol. José Ramón Acosta'),
              ('MA', 'Pol. Marta Abreu'), ('XX', 'Pol XX Aniversario'), ('CR', 'Pol Capitán Roberto Fleites'),
              ('CH', 'Pol. Chiqui Gómez Lubián'), ('LV', 'CPHEM VC'), ('EV', 'EMCOMED Villa Clara'),
              ('OC', 'Pol. Octavio de la Concepción y Pedraja'), ('MF', 'Pol. Manuel Fajardo Rivero'),
              ('HM', 'HMGD 26 de Diciembre'), ('XA', 'Pol. XXX Aniversario'), ('CC', 'Pol. Camilo Cienfuegos'),
              ('LF', 'Pol. Leandro Figueroa'), ('PA', 'Pol. Pablo Aguero'))

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    provincia = models.TextField(blank=True, null=True, choices=cprov)
    municipio = models.TextField(blank=True, null=True, choices=cmunic)
    sclinico = models.TextField(blank=True, null=True, choices=csitio)
    image = models.ImageField(default='default.jpg', upload_to='perfil_pics')
    history = HistoricalRecords()

    def __str__(self):
        return f'{self.user.username} Perfil'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
