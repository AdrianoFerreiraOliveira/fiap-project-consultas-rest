# Generated by Django 4.1.7 on 2023-03-24 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RestConsulta', '0003_alter_medico_rg'),
    ]

    operations = [
        migrations.AddField(
            model_name='medico',
            name='foto',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
