# Generated by Django 4.2.1 on 2023-07-04 00:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0017_curriculum_especialidad'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mecanico',
            name='cargo',
        ),
    ]
