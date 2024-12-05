from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from products.models import Product, ProductCategory


class IndexViewTestCase(TestCase):
    def test_index(self):
        path = reverse("products:index")
        response = self.client.get(path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data["title"], "Store")
        self.assertTemplateUsed(response, "products/index.html")


class ProductsListViewTestCase(TestCase):
    fixtures = ["fixtures/product-category-fixtures.json", "fixtures/products.json"]

    def setUp(self) -> None:
        self.product_category = ProductCategory.objects.all()
        self.products = Product.objects.all()

    def test_list(self):
        path = reverse("products:products")
        response = self.client.get(path)
        self.assertEqual(response.context_data["object_list"][0].name, "111")

        self._common_tests(response)
        self.assertEqual(
            list(response.context_data["object_list"]), list(self.products[:2])
        )

    def test_list_with_category(self):
        category = ProductCategory.objects.first()
        path = reverse("products:category", kwargs={"category_id": 1})
        response = self.client.get(path)

        self._common_tests(response)
        self.assertEqual(
            list(response.context_data["object_list"]),
            list(self.products.filter(category_id=category.id)),
        )

    def _common_tests(self, response):
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data["title"], "Products")
        self.assertTemplateUsed(response, "products/products.html")
