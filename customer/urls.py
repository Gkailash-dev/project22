from django.urls import path
from .views import*

urlpatterns=[
    path('orderlist/',order_list),
    path('order/',kailash),
    path('add/',customer_add),
    path('view/',customers),
    path('customer/delete/<int:id>/',delete,name='d_customer'),
    path('customer/update/<int:id>/',update,name='u_customer'),
    
]
