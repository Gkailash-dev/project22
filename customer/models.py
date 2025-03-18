from django.db import models
from backend.models import*

class Customer(models.Model):
    Customer_name=models.CharField(max_length=200,null=True)
    Customer_since=models.CharField(max_length=200,null=True)

    def __str__(self):
        return  self.Customer_name

class Order(models.Model):
    customer_reference=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    product_reference=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    order_number=models.CharField(max_length=200,null=True)
    order_date=models.DateField(default=0)
    order_quantity=models.FloatField(default=0)
    amount=models.FloatField(default=0)
    gst=models.FloatField(default=0)
    bill_amount=models.FloatField(default=0)

    def __str__(self):
        return  self.order_number
    


