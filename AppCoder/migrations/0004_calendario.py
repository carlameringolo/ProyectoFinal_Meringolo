# Generated by Django 4.2.6 on 2023-10-29 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0003_alter_sede_apertura'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calendario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia_semana', models.CharField(max_length=10)),
                ('hora_inicio', models.TimeField()),
                ('clase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppCoder.clases')),
            ],
        ),
    ]
