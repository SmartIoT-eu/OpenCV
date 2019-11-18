from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre")
    info = models.TextField(verbose_name="Información")
    image = models.ImageField(verbose_name="Image",upload_to="base")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")
    url = models.URLField(verbose_name="Enlace externo", blank=True, null=True)
    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "perfiles"
        ordering = ["-created"]
    def __str__(self):
        return self.name
