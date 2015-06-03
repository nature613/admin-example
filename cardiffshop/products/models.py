from django.db import models
from django.utils.encoding import smart_unicode
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):
    name = models.CharField(verbose_name=_("Name"), max_length=255)
    is_visible = models.BooleanField(verbose_name=_("Visible"), default=True)

    class Meta:
        verbose_name = _("Category")
        verbose_plural_name = _("Categories")
        ordering = ("name", )

    def __unicode__(self):
        return smart_unicode(self.name)


class Product(models.Model):
    name = models.CharField(verbose_name=_("Name"), max_length=255)
    category = models.ForeignKey(Category, verbose_name=_("Category"), related_name="products")
    price = models.DecimalField(max_digits=10, decimal_places=2, default="0.0")
    is_visible = models.BooleanField(verbose_name=_("Visible"), default=True)

    class Meta:
        verbose_name = _("Product")
        verbose_plural_name = _("Products")
        ordering = ("name", )

    def __unicode__(self):
        return smart_unicode(self.name)
