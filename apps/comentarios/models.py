from django.db import models
from apps.noticias.models import Noticia

# Create your models here.

class Comentario(models.Model):

    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE, related_name='comentario')
    comentario = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

