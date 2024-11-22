from django.urls import path

from products.views import IndexView, ProductsView

app_name = 'products'

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("products/", ProductsView.as_view(), name="products"),
]
