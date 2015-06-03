from products.models import Product, Category, ProductImage
from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from suit.admin import SortableTabularInline


class CanBeSoldListFilter(SimpleListFilter):
    title = "Can be sold"
    parameter_name = "can_be_sold"

    def lookups(self, request, model_admin):
        return (
            ("1", "Yes"),
            ("0", "No")
        )

    def queryset(self, request, queryset):
        value = self.value()
        if value == "1":
            return queryset.filter(stock_count__gt=0)
        if value == "0":
            return queryset.filter(stock_count=0)


class ProductImageInline(SortableTabularInline):
    model = ProductImage
    extra = 3
    ordering = ("order",)

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "stock_count", "can_be_sold")
    list_filter = ("category", "date_created", CanBeSoldListFilter)
    search_fields = ("name", "description", "sku_number", "barcode")
    inlines = (ProductImageInline, )

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
