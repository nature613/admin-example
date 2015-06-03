from products.models import Product, Category, ProductImage
from django.contrib import admin


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "stock_count", "can_be_sold")
    list_filter = ("category", "date_created")
    search_fields = ("name", "description", "sku_number", "barcode")
    fieldsets = (
        ("Identity", {
            "fields": ("name", "slug"),
        }),
        ("rr", {
            "fields": ("description", "price", "price_unit"),
        }),
        ("ww", {
            "fields": ("category", "barcode", "sku_number", "stock_count", "is_visible"),
        }),
    )

    def can_be_sold(self, obj):
        """
        Determines wheter the product can be sold or not.
        """
        if obj.stock_count > 0:
            return True
        else:
            return False

    can_be_sold.boolean = True


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
