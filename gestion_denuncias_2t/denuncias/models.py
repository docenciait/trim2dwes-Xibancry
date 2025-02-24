from django.db import models

# Create your models here.
class Denuncia(models.Model):
    CATEGORIAS = {"BC":"bache", "AL":"alumbrado", "BA":"basura", "OT":"otro"}
    
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField()
    imagen = models.ImageField(blank=True, null=True) # No tengo imagenes para testear, blank y null usados para hacer tests
    categoria = models.CharField(choices=CATEGORIAS, max_length=100)
    estado = models.CharField(default='pendiente', max_length=20)
    
    def __str__(self):
        return self.titulo