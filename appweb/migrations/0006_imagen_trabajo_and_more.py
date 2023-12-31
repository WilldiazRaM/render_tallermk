# Generated by Django 4.2.1 on 2023-06-21 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0005_contacto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='Trabajos')),
            ],
        ),
        migrations.CreateModel(
            name='Trabajo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('imagenes', models.ManyToManyField(related_name='trabajos', to='appweb.imagen')),
                ('mecanico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appweb.mecanico')),
            ],
        ),
        migrations.AlterField(
            model_name='administrador',
            name='trabajos_autorizados',
            field=models.ManyToManyField(related_name='administradores', to='appweb.trabajo'),
        ),
    ]
