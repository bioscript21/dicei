from django.db import models
from simple_history.models import HistoricalRecords
from simple_history import register
from django.contrib.auth.models import User
from PIL import Image

register(User)


class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
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
