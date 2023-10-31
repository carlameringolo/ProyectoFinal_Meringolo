from django.db import models
from django.contrib.auth.models import User

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
    duracion_choices=(
        ('30','30 minutos'),
        ('60','1 hora'),
        ('90', '1 hora y 30 minutos')
    )
    duracion=models.CharField(max_length=2, choices=duracion_choices)
    dificultad=models.IntegerField(choices=[(i,i) for i in range(1,11)],default=5)
    dia_choices=(
        ('Lunes','Lunes'),
        ('Martes','Martes'),
        ('Miercoles','Miercoles'),
        ('Jueves','Jueves'),
        ('Viernes','Viernes'),
        ('Sabado','Sabado')
    )
    dia=models.CharField(max_length=15, choices=dia_choices, default='Lunes')
    hora_inicio_choices=(
        ('8:00','8:00'),
        ('8:30','8:30'),
        ('9:00','9:00'),
        ('9:30','9:30'),
        ('10:00','10:00'),
        ('10:30','10:30'),
        ('11:00','11:00'),
        ('11:30','11:30'),
        ('12:00','12:00'),
        ('12:30','12:30'),
        ('13:00','13:00'),
        ('13:30','13:30'),
        ('14:00','14:00'),
        ('14:30','14:30'),
        ('15:00','15:00'),
        ('15:30','15:30'),
        ('16:00','16:00'),
        ('16:30','16:30'),
        ('17:00','17:00'),
        ('17:30','17:30'),
        ('18:00','18:00'),
        ('18:30','18:30'),
        ('19:00','19:00'),
        ('19:30','19:30'),
        ('20:00','20:00')

    )
    hora_inicio=models.CharField(max_length=10, choices=hora_inicio_choices, default='08:00')

    def __str__(self):
        return f'{self.nombre} - {self.hora_inicio} - {self.dia}'
    

class Sede(models.Model):
    localidad=models.CharField(max_length=20)
    telefono=models.IntegerField()
    mail=models.EmailField()
    apertura_choices=(
        ('6:30','6:30'),
        ('7am','7:00'),
        ('7:30','7:30'),
        ('8am', '8:00')
    )
    apertura=models.CharField(max_length=5, choices=apertura_choices)

    def __str__(self):
        return f'{self.localidad} - {self.apertura}'
    



class Avatar(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to='avatares', blank=True, null=True)
    def __str__(self):
        return f'{self.user}'



class Comentario(models.Model):
    nombre=models.CharField(max_length=40)
    mail=models.EmailField()
    comentario=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment[:50]