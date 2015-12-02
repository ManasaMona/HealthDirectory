# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthDirectory', '0002_auto_20151124_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service_provider',
            name='ser_email',
            field=models.EmailField(max_length=254),
        ),
    ]
