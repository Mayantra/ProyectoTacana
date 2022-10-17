# Generated by Django 4.1 on 2022-10-14 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_delete_avances'),
    ]

    operations = [
        migrations.CreateModel(
            name='avances',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=300, verbose_name='Titulo')),
                ('descripcion', models.TextField(blank=True, verbose_name='descripcion')),
                ('fechas', models.DateField(blank=True, verbose_name='Fecha')),
                ('foto', models.FileField(blank=True, upload_to='images/', verbose_name='Foto')),
                ('fecha_alta', models.DateTimeField(auto_now_add=True, verbose_name='Fecha alta')),
                ('fecha_actualizacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Actualizacion')),
            ],
        ),
    ]
