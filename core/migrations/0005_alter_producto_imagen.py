# Generated by Django 4.0.1 on 2022-06-25 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_carrito_id_alter_carrito_item_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.FileField(upload_to='core/static/core/img/productos'),
        ),
    ]