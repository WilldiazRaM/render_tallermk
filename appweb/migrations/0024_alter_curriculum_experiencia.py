# Generated by Django 4.2.1 on 2023-07-11 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0023_curriculum_rut'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curriculum',
            name='experiencia',
            field=models.TextField(max_length=2000),
        ),
    ]
