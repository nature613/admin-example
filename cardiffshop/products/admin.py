from products.models import Product, Category, ProductImage
from django.contrib import admin


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "stock_count", "can_be_sold")
    list_filter = ("category", "date_created")
    search_fields = ("name", "description", "sku_number", "barcode")

    readonly_fields = ("date_created", )
    fieldsets = (
        ("Identity", {
            'classes': ('suit-tab', 'suit-tab-identity',),
            "fields": ("category", "name", "slug"),
        }),
        ("Detail", {
            'classes': ('suit-tab', 'suit-tab-detail',),
            "fields": ("description", ("price", "price_unit")),
        }),
        ("Stock", {
            'classes': ('suit-tab', 'suit-tab-stock',),
            "fields": ("barcode", "sku_number", "stock_count"),
        }),
        (None, {
            "fields": ("is_visible", "date_created")
        })
    )

    suit_form_tabs = (
        ('identity', 'Identity'),
        ('detail', 'Detail'),
        ('stock', 'Stock')
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
