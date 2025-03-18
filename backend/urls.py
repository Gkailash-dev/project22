from django.urls import path
from .views import*


urlpatterns=[
   
   
    path('product/add/',product),
    path('product/view/',allproduct),
    path('product/delete/<int:id>/',Deleteproduct,name='p_delete'),
    path('product/update/<int:id>/',updateproduct,name='p_update'),


]