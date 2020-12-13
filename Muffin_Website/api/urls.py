from django.urls import path
from .views import MuffinView, CustomerView, OrderView, IndividualOrderView, CreateOrderView, CreateMuffinView

urlpatterns = [
    path('muffin', MuffinView.as_view()),
    path('customer', CustomerView.as_view()),
    path('order', OrderView.as_view()),
    path('individualorder', IndividualOrderView.as_view()),
    path('create-order', CreateOrderView.as_view()),
    path('create-muffin', CreateMuffinView.as_view())
]