# Generated by Django 4.0.4 on 2022-07-05 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webtaller', '0003_alter_atencion_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atencion',
            name='imagen',
            field=models.ImageField(default='nulo.jpg', null=True, upload_to='productos'),
        ),
    ]