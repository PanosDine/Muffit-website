from rest_framework import generics, status
from .serializers import MuffinSerializer, CustomerSerializer, OrderSerializer, IndividualOrderSerializer, CreateMuffinSerializer, CreateOrderSerializer
from .models import Muffin, Customer, Order, IndividualOrder
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404


class MuffinView(generics.ListAPIView):
    queryset = Muffin.objects.all()
    serializer_class = MuffinSerializer


class CustomerView(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class OrderView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class IndividualOrderView(generics.ListAPIView):
    queryset = IndividualOrder.objects.all()
    serializer_class = IndividualOrderSerializer

class CreateMuffinView(APIView):
    serializer_class = CreateMuffinSerializer
    def post(self, request, format=None):
        pass

class CreateOrderView(APIView):
    serializer_class = CreateOrderSerializer
    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            customer = serializer.data.get('customer')
            delivery_address = serializer.data.get('delivery_address')
            delivery_date = serializer.data.get('delivery_date')
            host = self.request.session.session_key
            queryset = Order.objects.filter(host=host)
            if queryset.exists():
                order = queryset[0]
                order.customer_id = get_object_or_404(Customer, name=customer)#Customer.objects.get(name=customer)
                order.delivery_address = delivery_address
                order.delivery_date = delivery_date
                order.save(update_fields=['customer_id', 'delivery_address', 'delivery_date'])
                return Response(OrderSerializer(order).data, status=status.HTTP_200_OK)
            else:
                order = Order(host=host, customer_id=get_object_or_404(Customer, name=customer), delivery_address=delivery_address, 
                delivery_date=delivery_date)
                order.save()
                return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)

        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)
