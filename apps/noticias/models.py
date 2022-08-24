from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length= 60)
    descripcion = models.CharField(max_length= 250, null=True, blank= True)

    def __str__(self):
        return self.nombre

class Noticia(models.Model):
    autor = models.CharField(max_length= 80, null=True, blank=True)
    titulo = models.CharField(max_length= 120)
    fecha_creacion = models.DateField(auto_now_add=True)
    detalle = models.TextField()
    imagen = models.ImageField(upload_to= 'noticias', default='noticias/default.jpg')
    categoria = models.ForeignKey(Categoria, on_delete = models.SET_NULL, null = True)

    def __str__(self):
        return self.titulo
