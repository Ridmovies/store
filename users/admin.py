from django.contrib import admin

from products.models import Basket
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    pass
