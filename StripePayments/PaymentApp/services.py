import stripe
from django.conf import settings
from django.db.models import Model

stripe.api_key = settings.STRIPE_SECRET_KEY


def get_instance(model: Model):
    return stripe.PaymentIntent.create(
        amount=model.total_price,
        currency=model.currency,
        payment_method_types=['card'],
    )
