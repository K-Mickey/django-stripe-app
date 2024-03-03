import stripe
from django.conf import settings

from ..models import Item


stripe.api_key = settings.STRIPE_SECRET_KEY


def get_instance(item: Item):
    return stripe.PaymentIntent.create(
        amount=item.price_int,
        currency=item.currency,
        payment_method_types=['card'],
    )
