from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    reseña = models.TextField()
    sinopsis = models.TextField()
    paginas = models.IntegerField()
    imagen = models.URLField(help_text="Pega la URL de la portada del libro")

    def __str__(self):
        return self.titulo
