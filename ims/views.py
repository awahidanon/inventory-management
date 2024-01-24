from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category, Department, Assign
from .forms import product_form, Assign_form
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils import timezone
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from xhtml2pdf import pisa
from django.core.files.base import ContentFile
import qrcode
from PIL import Image
import io




# Create your views here.
def index(request):
    assign = None
    error_message = None
    success_message = None
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
                success_message = "the product has been assigned." 

        else:
          error_message = "Insufficient quantity available." 

    form = Assign_form()

    context = {'product': product, 'department': department, 'form': form, 'assign': assign, 'error_message': error_message, 'success_message':success_message }

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


def generate_invoice(request, pro_id):
    assign = get_object_or_404(Assign, id=pro_id)

    generate_qr_code(assign)
    content = render_to_string('ims/invoice.html', {'assign': assign})

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename=invoice_{timezone.now()}.pdf'


    status = pisa.CreatePDF(content, dest=response)

    if status.err:
        return HttpResponse("Error creating PDF", status=500)

    return response






def generate_qr_code(assign):
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(f"Assign ID: {assign.id} \n Name: {assign.name}  \n product: {assign.product}  \n department: {assign.department}"  )
    qr.make(fit=True)

   
    img = qr.make_image(fill_color="black", back_color="white")

    
    img_bytes = io.BytesIO()
    img.save(img_bytes, format='PNG')

    
    assign.qr_code.save(f'qr_code_{assign.id}.png', ContentFile(img_bytes.getvalue()))