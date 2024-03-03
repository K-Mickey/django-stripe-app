from django.urls import path

from . import views


urlpatterns = [
    path('buy/<int:item_id>/', views.ItemBuyIdView.as_view(), name='buy'),
    path('item/<int:item_id>/', views.ItemView.as_view(), name='item'),
    path('success/', views.SuccessView.as_view(), name='success'),
    path('cancel/', views.CancelView.as_view(), name='cancel'),
]
