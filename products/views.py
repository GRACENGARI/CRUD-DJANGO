from django.shortcuts import render,redirect
from products.models import Product
from itertools import product
from itertools import product
from itertools import product

# Create your views here.
def home(request):
    return render(request, 'home.html')
def insert(request):
    return render(request, 'insert.html') 
# <!--function to  store data -->

def insert_data(request):
    if request.method=="POST":
        # capture user input
        prod_name=request.POST['prod_name']
        prod_price=request.POST['prod_price']
        prod_qty=request.POST['prod_qty']
        prod_desc=request.POST['prod_desc']
        prod_img=request.FILES['prod_img']

        # specify which column the data should go to 

        product =Product(
        
            prod_name=prod_name,
            prod_price=prod_price,
            prod_qty=prod_qty,
            prod_desc=prod_desc,
            prod_img=prod_img
            )
        # save user input
        product.save()
        return  redirect('/')
        
        
    return render(request, 'insert.html')
def view_products(request):
    products = Product.objects.all()
    return  render(request,'viewproducts.html',context={"products":products})