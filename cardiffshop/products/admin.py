from django.contrib import admin

# Register your models here.
from products.models import Product

admin.site.register(Product)