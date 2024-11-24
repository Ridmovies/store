from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, ListView

from products.models import Product, Basket


class IndexView(TemplateView):
    template_name = 'products/index.html'


class ProductsView(ListView):
    model = Product
    template_name = 'products/products.html'


@method_decorator(login_required, name='dispatch')
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


@method_decorator(login_required, name='dispatch')
def basket_remove(request: HttpRequest, basket_id: int) -> HttpResponse:
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return redirect(request.META.get('HTTP_REFERER'))


