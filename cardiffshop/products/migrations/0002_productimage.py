# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'/products/', verbose_name='Image')),
                ('order', models.IntegerField(default=0, verbose_name='Ordering')),
                ('alt_text', models.CharField(max_length=255, verbose_name='Alternative Text', blank=True)),
                ('product', models.ForeignKey(to='products.Product')),
            ],
            options={
                'ordering': ('order',),
                'verbose_name': 'Product Image',
                'verbose_name_plural': 'Product Images',
            },
        ),
    ]
