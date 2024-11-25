from django.contrib import admin

from products.models import Product, ProductCategory


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "price", "category", "quantity")
    fields = ("name", "description", "category", ("price", "quantity"))
    readonly_fields = ("description",)
    ordering = ("-name",)


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    pass
