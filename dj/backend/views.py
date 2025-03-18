from django.shortcuts import render,redirect
from.forms import*
from.models import*



def product(request):
    context={
        'product_form':Product_Form()
    }
    if request.method=="POST":
       product_form=Product_Form(request.POST)
       if product_form.is_valid():
          product_form.save()
    return render(request,'product_add.html',context)

def allproduct(request):
    context={
        "all_product":Product.objects.all()

    }
    return render(request,"allproduct.html",context)

def Deleteproduct(request,id):
    select_product=Product.objects.get(id=id)
    select_product.delete()
    return redirect('/backend/product/')

def updateproduct(request, id):
    select_product=Product.objects.get(id = id)
    context={
    "product_form": Product_Form(instance=select_product)
    }
    if request.method=='POST':
        product_form=Product_Form(request.POST,instance=select_product)
        if product_form.is_valid():
            product_form.save()
        return redirect('/backend/product/view')   
    return render(request,'product_add.html',context)

