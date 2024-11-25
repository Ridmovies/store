from django.contrib import admin

from products.models import Basket
from users.models import User


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ("product", "quantity")


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = [BasketAdmin]
