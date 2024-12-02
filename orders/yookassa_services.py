import os
import uuid

from django.conf import settings
from dotenv import load_dotenv
load_dotenv()

from yookassa import Configuration, Payment



Configuration.account_id = os.getenv("ACCOUNT_ID")
Configuration.secret_key = os.getenv("SECRET_KEY")


def get_confirmation_url(order_id: int, value: str, description: str):
    idempotence_key = str(uuid.uuid4())
    payment = Payment.create({
        "amount": {
            "value": value,
            "currency": "RUB"
        },
        "payment_method_data": {
            "type": "bank_card"
        },
        "confirmation": {
            "type": "redirect",
            "return_url": f'{settings.DOMAIN_NAME}',
        },
        "description": f"Заказ № {order_id}",
        "metadata": {"orderId": order_id},
        "capture": True,
        "test": True,
    }, idempotence_key)

    # get confirmation url
    confirmation_url = payment.confirmation.confirmation_url
    return confirmation_url, payment.id


def get_payment_info(payment_id: str):
    """ Получение информации о платеже """
    payment = Payment.find_one(payment_id)
    return payment