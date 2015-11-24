# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service_Provider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ser_name', models.CharField(max_length=50)),
                ('ser_spl', models.CharField(max_length=200)),
                ('ser_email', models.CharField(max_length=200)),
                ('ser_psword', models.CharField(max_length=200)),
                ('ser_phNum', models.CharField(max_length=15)),
                ('ser_addr', models.CharField(max_length=75)),
                ('ser_location', models.CharField(max_length=50)),
            ],
        ),
    ]
