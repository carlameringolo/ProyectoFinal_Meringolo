# Generated by Django 4.2.6 on 2023-10-29 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0006_clases_hora_inicio_alter_clases_dia'),
    ]

    operations = [
        migrations.AddField(
            model_name='clases',
            name='periodo',
            field=models.CharField(choices=[('Lunes', 'Lunes'), ('Martes', 'Martes'), ('Miercoles', 'Miercoles'), ('Jueves', 'Jueves'), ('Viernes', 'Viernes'), ('Sabado', 'Sabado')], default='Mañana', max_length=15),
        ),
        migrations.AlterField(
            model_name='clases',
            name='dia',
            field=models.CharField(choices=[('Lunes', 'Lunes'), ('Martes', 'Martes'), ('Miercoles', 'Miercoles'), ('Jueves', 'Jueves'), ('Viernes', 'Viernes'), ('Sabado', 'Sabado')], default='Lunes', max_length=15),
        ),
    ]