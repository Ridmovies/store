from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'products/index.html'


class ProductsView(TemplateView):
    template_name = 'products/products.html'
