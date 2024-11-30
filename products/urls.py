from django.urls import path
from django.views.decorators.cache import cache_page

from products.views import IndexView, ProductsView, basket_add, basket_remove

app_name = "products"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path(
        "products/category/<int:category_id>/", ProductsView.as_view(), name="category"
    ),
    path("products/", cache_page(30)(ProductsView.as_view()), name="products"),
    path("basket/add/<int:product_id>/", basket_add, name="basket_add"),
    path("basket/remove/<int:basket_id>/", basket_remove, name="basket_remove"),
]
