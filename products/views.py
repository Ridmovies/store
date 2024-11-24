from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView

from products.models import Product, Basket


class IndexView(TemplateView):
    template_name = 'products/index.html'


class ProductsView(ListView):
    model = Product
    template_name = 'products/products.html'


# class BasketListView(ListView):
#     queryset = Basket.objects.all()
#     template_name = 'products/baskets.html'
#     context_object_name = "baskets"


def basket_add(request: HttpRequest, product_id: int) -> HttpResponse:
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(
            user=request.user,
            product=product,
            quantity=1
        )
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    return redirect(request.META.get('HTTP_REFERER'))


def basket_remove(request: HttpRequest, basket_id: int) -> HttpResponse:
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return redirect(request.META.get('HTTP_REFERER'))


