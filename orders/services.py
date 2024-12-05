from orders.models import Order
from products.models import Basket
from products.services import get_total_sum


def update_success_order(user, order_id) -> None:
    order = Order.objects.get(id=order_id)
    baskets = Basket.objects.filter(user=user)
    order.basket_history = {
        "purchased_items": [basket.de_json() for basket in baskets],
        "total_sum": float(get_total_sum(baskets)),
    }
    baskets.delete()
    order.status = 1
    order.save()
