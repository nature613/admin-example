from django.db import models
from django.utils import timezone
from django.utils.encoding import smart_unicode
from django.utils.translation import ugettext_lazy as _

from products.constants import PRICE_UNIT_CHOICES, CAMPAIGN_CHOICES


class Category(models.Model):
    name = models.CharField(verbose_name=_("Name"), max_length=255)
    is_visible = models.BooleanField(verbose_name=_("Visible"), default=True)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        ordering = ("name", )

    def __unicode__(self):
        return smart_unicode(self.name)


class Product(models.Model):
    name = models.CharField(verbose_name=_("Name"), max_length=255)
    slug = models.SlugField(verbose_name=_("Slug"), max_length=255)
    description = models.TextField(_("Description"))
    category = models.ForeignKey(Category, verbose_name=_("Category"), related_name="products")

    campaign = models.CharField(_("Campaign"), choices=CAMPAIGN_CHOICES, blank=True, max_length=255)
    campaign_end_date = models.DateField(_("Campaign End Date"), blank=True, null=True)

    price = models.DecimalField(max_digits=10, decimal_places=2)
    price_unit = models.CharField(_("Price Unit"), choices=PRICE_UNIT_CHOICES, max_length=10)
    damaged = models.BooleanField(verbose_name=_("Damaged"), default=True,
                                  help_text="Only select this if all items are damaged.")


    sku_number = models.CharField(_("SKU number"), blank=True, null=False, max_length=255)
    barcode = models.CharField(_("Barcode"), max_length=255)
    stock_count = models.PositiveIntegerField(_("Stock Count"), default=0)

    is_visible = models.BooleanField(verbose_name=_("Visible"), default=True)
    date_created = models.DateTimeField(_("Date Created"), default=timezone.now)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        ordering = ("name",)

    def __unicode__(self):
        return smart_unicode(self.name)

    @models.permalink
    def get_absolute_url(self):
        return "product-detail", (self.slug, )


class ProductImage(models.Model):
    product = models.ForeignKey(Product)
    image = models.ImageField(verbose_name=_("Image"), upload_to="products/")
    order = models.IntegerField(verbose_name=_("Ordering"), default=0)
    alt_text = models.CharField(verbose_name=_("Alternative Text"), max_length=255, blank=True)

    class Meta:
        verbose_name = _("Product Image")
        verbose_name_plural = _("Product Images")
        ordering = ("order", )