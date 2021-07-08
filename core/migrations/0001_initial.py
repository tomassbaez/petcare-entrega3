# Generated by Django 3.2.5 on 2021-07-06 21:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('idMarca', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id')),
                ('nombreMarca', models.CharField(max_length=50, verbose_name='Marca')),
            ],
            options={
                'verbose_name': 'marca',
                'verbose_name_plural': 'marcas',
                'ordering': ['nombreMarca'],
            },
        ),
        migrations.CreateModel(
            name='Alimento',
            fields=[
                ('idAlimento', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Codigo')),
                ('descripcion', models.CharField(max_length=100, verbose_name='Descripción')),
                ('precio', models.IntegerField(verbose_name='Precio Unitario')),
                ('cantidad', models.IntegerField(verbose_name='Stock')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.marca')),
            ],
            options={
                'verbose_name': 'alimento',
                'verbose_name_plural': 'alimentos',
                'ordering': ['descripcion'],
            },
        ),
    ]
