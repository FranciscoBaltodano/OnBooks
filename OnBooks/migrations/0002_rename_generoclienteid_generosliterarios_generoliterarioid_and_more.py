# Generated by Django 4.1.7 on 2023-03-31 06:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OnBooks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='generosliterarios',
            old_name='GeneroClienteId',
            new_name='GeneroLiterarioId',
        ),
        migrations.RenameField(
            model_name='generosliterarios',
            old_name='GeneroName',
            new_name='GeneroLiterarioName',
        ),
    ]