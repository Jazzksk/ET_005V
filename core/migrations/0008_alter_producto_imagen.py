# Generated by Django 4.0.4 on 2022-07-12 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_suscripcion_compra_item_compra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.FileField(upload_to='imagenes/productos'),
        ),
    ]
