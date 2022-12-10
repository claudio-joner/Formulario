from django.db import models

# Create your models here.
class Usuario(models.Model):

    
    # Una clase típica definiendo un modelo, derivado desde la clase Model.
    
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    correo = models.CharField(max_length=25)

    class Meta:
        verbose_name =("Usuario")
        verbose_name_plural =("Usuarios")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("Usuario_detail", kwargs={"pk": self.pk})
