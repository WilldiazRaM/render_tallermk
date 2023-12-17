# Generated by Django 4.2.1 on 2023-06-07 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0002_mecanico_foto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mecanico',
            old_name='fecha',
            new_name='fecha_nacimiento',
        ),
        migrations.AddField(
            model_name='mecanico',
            name='edad',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='mecanico',
            name='email',
            field=models.EmailField(default='example@example.com', max_length=254),
        ),
        migrations.AddField(
            model_name='mecanico',
            name='especialista',
            field=models.CharField(default='Sin especialidad', max_length=100),
        ),
        migrations.AddField(
            model_name='mecanico',
            name='rut',
            field=models.CharField(default='1-0', max_length=70),
        ),
    ]
