from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from products.models import Product


class IndexView(TemplateView):
    template_name = 'products/index.html'


class ProductsView(ListView):
    model = Product
    # queryset = Product.objects.all()
    template_name = 'products/products.html'
