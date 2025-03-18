from django.shortcuts import render,redirect
from .forms import*
from .models import*

def customer_add(request):
    context={
       "customer_form":Customer_Form() 
       }
    if request.method=="POST":
       C=Customer_Form(request.POST)
       C.save()
    return render(request,"customer.html",context)



def customers(request):
    context={
        "all_customer":Customer.objects.all()

    }
    return render(request,'all_customer.html',context)


def delete(request,id):
     select_product=Customer.objects.get(id=id)
     select_product.delete()
     return redirect('/customer/view/')



def update(request,id):
    select_customer=Customer.objects.get(id=id)
    context={
      "customer_form":Customer_Form(instance=select_customer)

       }
    if request.method == 'POST':
        customer_for=Customer_Form(request.POST,instance=select_customer)
        if customer_for.is_valid():
           customer_for.save()
           return redirect('/customer/view/')   
    return render(request,'customer.html',context)
    
def kailash(request):
    context={
        "order_form":Order_Form()
    }
 # it get the  data for which  one  is  selected
    if request.method=='POST':
       selected_product=Product.objects.get(id  = request.POST['product_reference'])
       selected_customer=Customer.objects.get(id  = request.POST['customer_reference'])
       amount=float(selected_product.price) *  float(request.POST['order_quantity'])  
       gst=(amount*selected_product.gst)/100
       bill_amount=amount+gst
#then store  data  database
       new_order=Order(customer_reference_id = request.POST['customer_reference'],
     product_reference_id = request.POST['product_reference'],order_number=request.POST['order_number'],
        order_date=request.POST['order_date'],order_quantity=request.POST['order_quantity'],amount=amount,gst=gst,bill_amount=bill_amount)
       new_order.save()
    return  render(request,"order_add.html",context)


#used to  show  the  data in database
def order_list(request):
    context={
        "order_list":Order.objects.all()
    }
    return render(request,'order.html',context)
    
#delete the  order

