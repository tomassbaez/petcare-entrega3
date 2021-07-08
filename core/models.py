from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.
#creacion de 5 tablas 
#MARCA,ALIMENTO_PERRO_GATO, ACCESORIOS_PERRO_GATOS, LIMPIEZA, PELUQUERIA(tijera, maquinas)
#CADA TABLA CORRESPONDE A UN TIPO DE PRODUCTO
#ALIMENTPO_PERRO = ID(PK), MARCA, DESCRIPCION, PRECIO

# Create your models here.

#TABLA MARCA
class Marca(models.Model):
    idMarca = models.IntegerField(primary_key=True, verbose_name='Id')
    nombreMarca = models.CharField(max_length=50, verbose_name="Marca")

    class Meta:
        verbose_name = 'marca'
        verbose_name_plural = 'marcas'
        ordering = ["nombreMarca"]

    def __str__(self):
        return self.nombreMarca

#TABLA ALIMENTO
class Alimento(models.Model):
    idAlimento = models.CharField(primary_key=True, max_length=10, verbose_name='Codigo' )
    descripcion = models.CharField(max_length=100,verbose_name='Descripción')
    precio = models.IntegerField(verbose_name='Precio Unitario')
    cantidad = models.IntegerField(verbose_name='Stock')
    imagen = models.ImageField(verbose_name='Imagen',upload_to='alimentos',null=True,blank=True)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'alimento'
        verbose_name_plural = 'alimentos'
        ordering = ["descripcion"]

    def __str__(self):
            return self.descripcion

#TABLA ACCESORIO
class Accesorio(models.Model):
    idAccesorio = models.CharField(primary_key=True, max_length=10, verbose_name='Codigo' )
    descripcion = models.CharField(max_length=100,verbose_name='Descripción')
    precio = models.IntegerField(verbose_name='Precio Unitario')
    cantidad = models.IntegerField(verbose_name='Stock')
    imagen = models.ImageField(verbose_name='Imagen',upload_to='accesorios',null=True,blank=True)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'accesorio'
        verbose_name_plural = 'accesorios'
        ordering = ["descripcion"]

    def __str__(self):
            return self.descripcion

#TABLA LIMPIEZA
class Producto_limpieza(models.Model):
    idProducto_limpieza = models.CharField(primary_key=True, max_length=10, verbose_name='Codigo' )
    descripcion = models.CharField(max_length=100,verbose_name='Descripción')
    precio = models.IntegerField(verbose_name='Precio Unitario')
    cantidad = models.IntegerField(verbose_name='Stock')
    imagen = models.ImageField(verbose_name='Imagen',upload_to='productos_limpieza',null=True,blank=True)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'producto_limpieza'
        verbose_name_plural = 'productos_limpieza'
        ordering = ["descripcion"]

    def __str__(self):
            return self.descripcion

#TABLA PELUQUERIA
class Producto_peluqueria(models.Model):
    idProducto_peluqueria = models.CharField(primary_key=True, max_length=10, verbose_name='Codigo' )
    descripcion = models.CharField(max_length=100,verbose_name='Descripción')
    precio = models.IntegerField(verbose_name='Precio Unitario')
    cantidad = models.IntegerField(verbose_name='Stock')
    imagen = models.ImageField(verbose_name='Imagen',upload_to='productos_peluqueria',null=True,blank=True)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'producto_peluqueria'
        verbose_name_plural = 'productos_peluqueria'
        ordering = ["descripcion"]

    def __str__(self):
            return self.descripcion

