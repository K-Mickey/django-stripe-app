from django.urls import path

from . import views


urlpatterns = [
    path('buy/<int:pk>/', views.GetBuyIdView.as_view()),
]
