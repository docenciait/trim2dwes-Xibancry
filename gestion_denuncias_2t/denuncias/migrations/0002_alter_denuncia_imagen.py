# Generated by Django 5.0.12 on 2025-02-24 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('denuncias', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='denuncia',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
