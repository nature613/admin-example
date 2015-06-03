# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='campaign',
            field=models.CharField(blank=True, max_length=255, verbose_name='Campaign', choices=[(b'', 'No Campaign'), (b'10-percent-off', '10% off'), (b'2-for-1', '2 for 1'), (b'3-for-2', 'Buy 2 get 3')]),
        ),
        migrations.AddField(
            model_name='product',
            name='campaign_end_date',
            field=models.DateField(null=True, verbose_name='Campaign End Date', blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='damaged',
            field=models.BooleanField(default=True, help_text=b'Only select this if all items are damaged.', verbose_name='Damaged'),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date Created'),
        ),
    ]
