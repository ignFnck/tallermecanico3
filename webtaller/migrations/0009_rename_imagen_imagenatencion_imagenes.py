# Generated by Django 4.0.4 on 2022-07-13 04:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webtaller', '0008_alter_imagenatencion_atencion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imagenatencion',
            old_name='imagen',
            new_name='imagenes',
        ),
    ]
