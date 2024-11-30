from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from common.mixins import TitleMixin
from orders.forms import OrderForm
from orders.models import Order


class OrderCreateView(TitleMixin, CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'orders/order-create.html'
    success_url = reverse_lazy('orders:order_create')
    title = 'Store: Create Order'

    def form_valid(self, form):
        form.instance.initiator = self.request.user
        return super().form_valid(form)

