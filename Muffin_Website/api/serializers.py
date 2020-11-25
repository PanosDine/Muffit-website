from rest_framework import serializers
from .models import Muffin, Customer, Order, IndividualOrder

class MuffinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Muffin 
        fields = ('id', 'muffin_name', 'muffin_price')

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer 
        fields = ('id', 'name', 'address', 
        'postcode', 'email', 'phone')

class OrderSerializer(serializers.ModelSerializer):
    customer = serializers.Field
    class Meta:
        model = Order 
        fields = ('id', 'host', 'code', 
        'delivery_address', 'delivery_date', 'customer')

class IndividualOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndividualOrder 
        fields = ('id', 'quantity', 'unit_price', 'discount')

class CreateMuffinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Muffin
        fields = ('muffin_name', 'muffin_price')

class CreateOrderSerializer(serializers.ModelSerializer):
    #customer = serializers.Field(source='customer.name') 
    #this line allows me to
    #freely allocate a new customer name without it already existing in the db
    class Meta:
        model = Order
        fields = ('delivery_address', 'delivery_date', 'customer')