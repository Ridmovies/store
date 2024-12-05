from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.generic import ListView, TemplateView

from common.mixins import TitleMixin
from products.models import Basket, Product, ProductCategory


class IndexView(TitleMixin, TemplateView):
    template_name = "products/index.html"
    title = "Store"


class ProductsView(ListView):
    model = Product
    template_name = "products/products.html"
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = cache.get("categories")
        if categories is None:
            context["categories"] = ProductCategory.objects.all()
            cache.set("categories", context["categories"], 30)
        else:
            context["categories"] = categories
        context["title"] = "Products"
        return context

    def get_queryset(self):
        # Получаем category_id из URL
        category_id = self.kwargs.get("category_id")
        if category_id is not None:
            # Фильтруем продукты по указанной категории
            queryset = Product.objects.filter(category__id=category_id)
        else:
            # Если категория не указана, возвращаем все продукты
            queryset = super().get_queryset()
        return queryset.order_by("id")


def basket_add(request: HttpRequest, product_id: int) -> HttpResponse:
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    return redirect(request.META.get("HTTP_REFERER"))


def basket_remove(request: HttpRequest, basket_id: int) -> HttpResponse:
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return redirect(request.META.get("HTTP_REFERER"))
