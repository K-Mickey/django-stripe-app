from django.http import JsonResponse
from django.views.generic import DetailView

from .models import Item
from .services import item_service


class GetBuyIdView(DetailView):
    model = Item

    def get(self, request, *args, **kwargs):
        item = self.get_object()
        intent = item_service.get_instance(item)
        return JsonResponse({
            'client_secret': intent.client_secret,
        })
