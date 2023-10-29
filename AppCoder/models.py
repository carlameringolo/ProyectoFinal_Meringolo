from django.db import models

# Create your models here.

class Entrenador(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    especialidad=models.CharField(max_length=40)
    
    def __str__(self):
        return f'{self.nombre} {self.apellido} - {self.especialidad}'

class Cliente(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    dni=models.IntegerField()
    aptoFisico=models.BooleanField(default=False)

    def __str__(self):
        return f'{self.nombre} {self.apellido} - {self.aptoFisico}'
    

class Clases(models.Model):
    nombre=models.CharField(max_length=40)
    duracion=models.DurationField()
    dificultad=models.IntegerField(choices=[(i,i) for i in range(1,11)],default=5)

    def __str__(self):
        return f'{self.nombre} - {self.duracion}'
    

class Sede(models.Model):
    localidad=models.CharField(max_length=20)
    telefono=models.IntegerField()
    mail=models.EmailField()
    apertura=models.TimeField()

    def __str__(self):
        return f'{self.localidad} - {self.apertura}'
    



