from django.urls import path

from products.views import (
    IndexView,
    ProductsView,
    basket_add,
    basket_remove,
)

app_name = 'products'

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("products/category/<int:category_id>/", ProductsView.as_view(), name="category"),
    path("products/", ProductsView.as_view(), name="products"),
    # path("basket/", BasketListView.as_view(), name="basket"),
    path("basket/add/<int:product_id>/", basket_add, name="basket_add"),
    path("basket/remove/<int:basket_id>/", basket_remove, name="basket_remove"),
]
