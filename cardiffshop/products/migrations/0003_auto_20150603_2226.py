# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_productimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='barcode_number',
        ),
        migrations.AddField(
            model_name='product',
            name='barcode',
            field=models.CharField(default='', max_length=255, verbose_name='Barcode'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='stock_count',
            field=models.PositiveIntegerField(default=0, verbose_name='Stock Count'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(upload_to=b'products/', verbose_name='Image'),
        ),
    ]
