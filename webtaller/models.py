from django.db import models

# Create your models here.
class Categoria(models.Model):
    tipovehiculo= models.CharField(primary_key=True,max_length=20)

    def __str__(self):
        return self.tipovehiculo

class tipoAte(models.Model):
    tipoate= models.CharField(primary_key=True,max_length=20)
    
    def __str__(self):
        return self.tipoate
##############################################################
class Atencion(models.Model):
    id = models.IntegerField(null=False, primary_key=True)
    tipoate= models.ForeignKey(tipoAte,on_delete=models.CASCADE)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='productos',null=True,default='nulo.jpg')
    publicar = models.BooleanField(default=False)
    comentario = models.TextField()
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    usuario = models.CharField(max_length=60,default='--')

    def __str__(self):
        return self.usuario

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField()
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre


class ImagenAtencion(models.Model):
    imagens = models.ImageField(upload_to='productos')
    atencion = models.ForeignKey(Atencion, on_delete=models.CASCADE, related_name="imagenes")