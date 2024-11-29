from django.contrib import admin

from products.models import Basket
from users.models import User, EmailVerification


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ("product", "quantity")


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = [BasketAdmin]


@admin.register(EmailVerification)
class EmailVerificationAdmin(admin.ModelAdmin):
    pass
