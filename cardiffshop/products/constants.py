from django.utils.translation import ugettext_lazy as _

PRICE_UNIT_CHOICES = (
    ("GBP", _("Pounds")),
    ("USD", _("US Dollars")),
    ("EUR", _("Euro"))
)

CAMPAIGN_CHOICES = (
    ("", _("No Campaign")),
    ("10-percent-off", _("10% off")),
    ("2-for-1", _("2 for 1")),
    ("3-for-2", _("Buy 2 get 3")),
)