from django.urls import path

from . import views


urlpatterns = [
    path('order/<int:order_id>/', views.OrderView.as_view(), name='order'),
    path('order-buy/<int:order_id>/', views.OrderBuyIdView.as_view(), name='order-buy'),
    path('buy/<int:item_id>/', views.ItemBuyIdView.as_view(), name='buy'),
    path('item/<int:item_id>/', views.ItemView.as_view(), name='item'),
    path('success/', views.SuccessView.as_view(), name='success'),
    path('cancel/', views.CancelView.as_view(), name='cancel'),
]
