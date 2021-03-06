# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-06 20:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subsidio',
            fields=[
                ('Cod_cliente', models.IntegerField(primary_key=True, serialize=False)),
                ('Dummy', models.IntegerField()),
                ('Nombre', models.CharField(max_length=100)),
                ('Fecha', models.DateField()),
                ('Plazo', models.IntegerField()),
                ('SubsidioEntregado', models.FloatField()),
                ('SubsidioUtilizado', models.FloatField()),
                ('SubsidioDisponible', models.FloatField()),
            ],
        ),
    ]
