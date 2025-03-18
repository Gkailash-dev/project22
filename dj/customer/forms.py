from django.forms import ModelForm
from.models import*
class Customer_Form(ModelForm):
    class Meta:
        model=Customer
        fields="__all__"

class Order_Form(ModelForm):
    class Meta:
        model=Order
        fields=["customer_reference","product_reference","order_number","order_date","order_quantity"]