from products.models import Product
from django.views.generic import DetailView


class ProductDetail(DetailView):
    template_name = "products/detail.html"
    model = Product
    slug_field = "slug"
    context_object_name = "product"