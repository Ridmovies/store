from django.urls import path

from orders.views import OrderCreateView, order_payment, check_payment

app_name = "orders"

urlpatterns = [
    path('order_create/', OrderCreateView.as_view(), name='order_create'),
    path('order_payment/', order_payment, name='order_payment'),
    path('check_payment/<str:payment_id>/', check_payment, name='check_payment'),
]
