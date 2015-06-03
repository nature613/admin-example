# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('is_visible', models.BooleanField(default=True, verbose_name='Visible')),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('slug', models.SlugField(max_length=255, verbose_name='Slug')),
                ('description', models.TextField(verbose_name='Description')),
                ('price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('price_unit', models.CharField(max_length=10, verbose_name='Price Unit', choices=[(b'GBP', 'Pounds'), (b'USD', 'US Dollars'), (b'EUR', 'Euro')])),
                ('sku_number', models.CharField(max_length=255, verbose_name='SKU number', blank=True)),
                ('barcode', models.CharField(max_length=255, verbose_name='Barcode')),
                ('stock_count', models.PositiveIntegerField(default=0, verbose_name='Stock Count')),
                ('is_visible', models.BooleanField(default=True, verbose_name='Visible')),
                ('date_created', models.DateTimeField(auto_now=True, verbose_name='Date Created')),
                ('category', models.ForeignKey(related_name='products', verbose_name='Category', to='products.Category')),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'products/', verbose_name='Image')),
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
