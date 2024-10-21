from django.db import models

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Marca(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    TAMAÑOS = (
        ('P', 'Pequeño'),
        ('M', 'Mediano'),
        ('G', 'Grande'),
    )

    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    precio = models.IntegerField(blank=False, null=False)
    tamaño = models.CharField(max_length=1, choices=TAMAÑOS)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
   

    def __str__(self):
        return self.nombre
