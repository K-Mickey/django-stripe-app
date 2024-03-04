from django.conf import settings
from django.http import JsonResponse
from django.views.generic import DetailView, TemplateView

from .models import Item, Order
from .services import get_instance


class OrderView(DetailView):
    model = Order
    pk_url_kwarg = 'order_id'
    context_object_name = 'order'
    template_name = 'order.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['publishable_key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context


class OrderBuyIdView(DetailView):
    model = Order
    pk_url_kwarg = 'order_id'

    def get(self, request, *args, **kwargs):
        order = self.get_object()
        intent = get_instance(order)
        return JsonResponse({
            'client_secret': intent.client_secret,
        })


class ItemView(DetailView):
    model = Item
    pk_url_kwarg = 'item_id'
    context_object_name = 'item'
    template_name = 'item.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['publishable_key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context


class ItemBuyIdView(DetailView):
    model = Item
    pk_url_kwarg = 'item_id'

    def get(self, request, *args, **kwargs):
        item = self.get_object()
        intent = get_instance(item)
        return JsonResponse({
            'client_secret': intent.client_secret,
        })


class SuccessView(TemplateView):
    template_name = 'success.html'


class CancelView(TemplateView):
    template_name = 'cancel.html'
