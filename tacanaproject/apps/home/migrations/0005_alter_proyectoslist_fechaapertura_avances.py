# Generated by Django 4.1 on 2022-10-14 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_tipoproyecto_proyectoslist_tipoproyecto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyectoslist',
            name='fechaApertura',
            field=models.DateField(blank=True, verbose_name='FechaFinal'),
        ),
        migrations.CreateModel(
            name='avances',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=300, verbose_name='Titulo')),
                ('descripcion', models.TextField(blank=True, verbose_name='descripcion')),
                ('fecha', models.DateField(blank=True, verbose_name='fecha')),
                ('foto', models.FileField(blank=True, upload_to='images/', verbose_name='Foto')),
                ('fecha_alta', models.DateTimeField(auto_now_add=True, verbose_name='Fecha alta')),
                ('fecha_actualizacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Actualizacion')),
                ('proyecto', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='home.proyectoslist')),
            ],
        ),
    ]
