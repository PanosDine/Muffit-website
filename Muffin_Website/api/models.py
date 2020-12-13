from django.db import models
import string
import random
from phonenumber_field.modelfields import PhoneNumberField

def generate_unique_code():
    length = 6

    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Order.objects.filter(code=code).count() == 0:
            break
    return code


class Muffin(models.Model):
    muffin_name = models.CharField(max_length=50, unique=True)
    muffin_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.muffin_name



class Customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    postcode = models.CharField(max_length=10)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=50, unique=True)
    phone = PhoneNumberField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name #if self.name else 'New Customer'


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    host = models.CharField(max_length=50, unique=True)
    code = models.CharField(max_length=6, default=generate_unique_code, unique=True)
    delivery_address = models.CharField(max_length=50)
    delivery_date = models.DateTimeField('Delivery date & time')

    def __str__(self):
        return self.code


class IndividualOrder(models.Model):
    muffin = models.ForeignKey(Muffin, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    unit_price = Muffin.muffin_price
    discount = models.DecimalField(max_digits=4, decimal_places=2, default=0)

    def __str__(self):
        return 'variant'
