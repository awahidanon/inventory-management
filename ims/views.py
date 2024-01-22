from django.shortcuts import render, redirect
from .models import Product, Category, Department, Assign
from .forms import product_form, Assign_form


# Create your views here.
def index(request):
    assign = None
    error_message = None
    product  = Product.objects.all()
    department = Department.objects.all()
    if request.method == 'POST':
        form = Assign_form(request.POST)
        if form.is_valid():
            assign = form.save(commit=False) 
            productassign = assign.product
            if productassign.quantity >= assign.quantity:
                productassign.quantity -= assign.quantity
                productassign.save()
                assign.save()

        else:
          error_message = "Insufficient quantity available." 

    form = Assign_form()

    context = {'product': product, 'department': department, 'form': form, 'assign': assign, 'error_message': error_message }

    return render(request, 'ims/index.html', context)

def assigned_product(request):
    product = Assign.objects.all()
    context = { 'assigned_product':product}
    return render(request, 'ims/products.html', context)

def add_product(request):
    success_message = None
    error_message = None
    if request.method == "POST":
       form = product_form(request.POST)
       if form.is_valid():
           form.save()
           success_message = "successfully created!"
       error_message = "faild to add!"
    else:
        
        form = product_form()
        
    context =  {"form": form, 'success_message':success_message, 'error_message':error_message}

    return render(request, "ims/addproduct.html", context)

def product_detail(request, pk):
    product = Product.objects.filter(id = pk)
    context = {'product': product}
    return render(request, "ims/details.html", context)

#delete store products
def delete(request,pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('index')
    return render(request, 'ims/delete.html',{'obj':product})

#delete assined products
def delete_product(request,pk):
    product = Assign.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product')
    
    return render(request, 'ims/delete.html',{'obj':product})

#delete store products
def update(request, pk):
    success_message = None
    project = Product.objects.get(id=pk)
    form = product_form(instance=project)
    if request.method == 'POST':
        form = product_form(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('index')
        success_message = "Product successfully Updated!"
    context = {'form': form, 'success_message': success_message}
    
    return render(request, 'ims/addproduct.html', context)

#update assined products
def update_product(request, pk):
    success_message = None
    project = Assign.objects.get(id=pk)
    form = Assign_form(instance=project)
    if request.method == 'POST':
        form =Assign_form(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('product')
        success_message = "Product successfully Updated!"
    context = {'form': form, 'success_message': success_message}
    
    return render(request, 'ims/assign.html', context)