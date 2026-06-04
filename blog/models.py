from django.db import models
from django.utils import timezone   

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(default=timezone.now)
    archivo = models.FileField(upload_to='archivos/', null=True, blank=True)

    def __str__(self):
        return self.titulo
# Create your models here.
