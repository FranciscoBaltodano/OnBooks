# Generated by Django 4.1.7 on 2023-03-31 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autores',
            fields=[
                ('AutorId', models.AutoField(primary_key=True, serialize=False)),
                ('AutorName', models.CharField(max_length=500)),
                ('AutorDate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Ciudades',
            fields=[
                ('CiudadId', models.AutoField(primary_key=True, serialize=False)),
                ('CiudadName', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Editoriales',
            fields=[
                ('EditorialId', models.AutoField(primary_key=True, serialize=False)),
                ('EditorialName', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='GenerosClientes',
            fields=[
                ('GeneroClienteId', models.AutoField(primary_key=True, serialize=False)),
                ('GeneroName', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='GenerosLiterarios',
            fields=[
                ('GeneroClienteId', models.AutoField(primary_key=True, serialize=False)),
                ('GeneroName', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Idiomas',
            fields=[
                ('IdiomaId', models.AutoField(primary_key=True, serialize=False)),
                ('IdiomaName', models.CharField(max_length=500)),
            ],
        ),
    ]