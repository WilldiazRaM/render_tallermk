# Generated by Django 4.2.1 on 2023-06-21 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0006_imagen_trabajo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='administrador',
            name='motivo_rechazo',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='trabajo',
            name='autorizado',
            field=models.BooleanField(default=False),
        ),
    ]
