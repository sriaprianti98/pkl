# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pengumuman',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('judul_pengumuman', models.CharField(max_length=45)),
                ('tanggal', models.DateField()),
                ('jam', models.TimeField()),
            ],
        ),
    ]
