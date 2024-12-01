from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from common.mixins import TitleMixin
from orders.forms import OrderForm
from orders.models import Order
from orders.yookassa_services import get_confirmation_url, get_payment_info
from products.models import Basket
from products.services import get_total_sum


class OrderCreateView(TitleMixin, CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'orders/order-create.html'
    success_url = reverse_lazy('orders:order_payment')
    title = 'Store: Create Order'

    def form_valid(self, form):
        form.instance.initiator = self.request.user
        return super().form_valid(form)


def order_payment(request):
    order = Order.objects.filter(initiator=request.user).last()
    baskets = Basket.objects.filter(user=request.user)
    value: str = str(get_total_sum(baskets))
    description = order.id
    url = get_confirmation_url(order.id, value, description)
    return redirect(url)


def check_payment(request, payment_id: str):
    payment_info = get_payment_info(payment_id)
    order_id = payment_info.metadata.get("orderId")
    # order = Order.objects.get(id=order_id)
    print(f"{payment_info.status=}")
    if payment_info.status == "succeeded":
        baskets = Basket.objects.filter(user=request.user)
        baskets.delete()
    else:
        pass
    return redirect("products:index")
