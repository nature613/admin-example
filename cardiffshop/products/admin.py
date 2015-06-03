from django.contrib import admin
from products.models import Category, Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category")
    list_filter = ("category", "date_created")
    search_fields = ("name", "description", "sku_number", "barcode_number")


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
