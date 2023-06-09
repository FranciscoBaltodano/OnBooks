# Generated by Django 4.1.7 on 2023-04-06 04:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('OnBooks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='autores',
            name='AutorDate',
        ),
        migrations.CreateModel(
            name='Libros',
            fields=[
                ('LibroId', models.AutoField(primary_key=True, serialize=False)),
                ('LibroName', models.CharField(max_length=200)),
                ('LibroAutor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='OnBooks.autores')),
                ('LibroEditorial', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='OnBooks.editoriales')),
                ('LibroGenero', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='OnBooks.generosliterarios')),
                ('LibroIdioma', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='OnBooks.idiomas')),
            ],
        ),
    ]
