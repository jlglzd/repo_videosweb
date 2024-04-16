from django.db import models

# Create your models here.

class Genre(models.Model):
    """Modelo que representa una descripcion del tipo de video (p. ej. Fam. Torres Cuevas, Fam. Gonzalez Torres, Cumpleanos, Don Chuy, etc.)."""
    nombre = models.CharField(max_length=200, help_text="Ingrese el nombre del tipo de video (p. ej. Fam. Gonzalez Torres, Cumpleanos, etc.)")


    def __str__(self):
        """Cadena que representa a la instancia particular del modelo (p. ej. en el sitio de Administracion)"""

        return self.nombre

from django.urls import reverse #Used to generate URLs by reversing the URL patterns

class Video(models.Model):
    """Modelo que representa un video (pero no un video especifico)."""

    titulo = models.CharField(max_length=200)

    autor = models.ForeignKey('Autor', on_delete=models.SET_NULL, null=True)
    # ForeignKey, ya que un libro tiene un solo autor, pero el mismo autor puede haber escrito muchos libros.
    # 'Autor' es un string, en vez de un objeto, porque la clase Author aun no ha sido declarada.

    resumen = models.TextField(max_length=1000, help_text="Ingrese una breve descripcion del video")

    genero = models.ManyToManyField(Genre, help_text="Seleccione un genero para este video")
    # ManyToManyField, porque un genero puede contener muchos videos y un video puede cubrir varios generos.
    # La clase Genre ya ha sido definida, entonces podemos especificar el objeto arriba.

    def __str__(self):
        """String que representa al objeto Video"""
        return self.titulo


    def get_absolute_url(self):
        """Devuelve el URL a una instancia particular de Video"""
        return reverse('video-detail', args=[str(self.id)])

import uuid # Requerida para las instancias de libros unicos

class VideoInstancia(models.Model):
    """Modelo que representa una copia especifica de un video (i.e. que puede ser prestado por la biblioteca de videos)."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID unico para este video particular en toda la biblioteca")
    video = models.ForeignKey('Video', on_delete=models.SET_NULL, null=True)

    LOAN_STATUS = (
        ('m', 'Mantenimiento'),
        ('o', 'Viendo'),
        ('a', 'Disponible'),
        ('r', 'Reservado'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Disponibilidad del video')

    class Meta:
        ordering = ["video"]


    def __str__(self):
        """String para representar el Objeto del Modelo"""
        return '%s (%s)' % (self.id,self.video.titulo)

class Autor(models.Model):
    """Modelo que representa un autor"""
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    fecha_de_nacimiento = models.DateField(null=True, blank=True)

    def get_absolute_url(self):
        """Retorna la url para acceder a una instancia particular de un autor."""
        return reverse('autor-detail', args=[str(self.id)])


    def __str__(self):
        """String para representar el Objeto Modelo"""
        return '%s, %s' % (self.nombre, self.apellidos)
