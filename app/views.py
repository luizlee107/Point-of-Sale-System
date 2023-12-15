from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from .models import *

def pos(request):
    # Initialize variables
    cart_items = []
    cart_total = 0
    form = PosForm(request.POST or None)
    products = Product.objects.all()  

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('product_list')
        
        # Process form data here if needed
        
    # Populate cart_items with all filtered products
    for product in products:
        cart_items.append({
            'name': product.name,
            'price_unit': product.price,
            'quantity2': 1,
            'total': product.price * 1,
        })
    
    # Calculate cart total
    cart_total = sum(item['total'] for item in cart_items)    

    context = {
        'cart_items': cart_items,
        'cart_total': cart_total,
        'form': form,
        'products': products,
    }

    return render(request, 'pos.html', context)


    
def products2(request):
    if request.method == 'GET':
        name_to_filter = request.GET.get('name') 
        barcode_to_filter=request.GET.get('barcode')
        
        if name_to_filter:
            products = Product.objects.filter(name__icontains=name_to_filter) 
           
        elif barcode_to_filter:
             products = Product.objects.filter(barcode__icontains=barcode_to_filter) 
        else:
            products = Product.objects.all()
        
        return render(request, 'popup_content.html', {'products': products})
    

    
def products(request):
    if request.method == 'GET':
        name_to_filter = request.GET.get('name') 
        barcode_to_filter=request.GET.get('barcode')
        
        if name_to_filter:
            products = Product.objects.filter(name__icontains=name_to_filter) 
           
        elif barcode_to_filter:
             products = Product.objects.filter(barcode__icontains=barcode_to_filter) 
        else:
            products = Product.objects.all()
        
        return render(request, 'products.html', {'products': products})
    

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('create_product')  # Redirect to a view that lists products0
    else:
        form = ProductForm()

    return render(request, 'create_product.html', {'form': form})


def delete_product(request,pk=None):
    Product.objects.get(id=pk).delete()
    return redirect('products.html')

def update_product(request,pk=None):
    Product.objects.get(id=pk).delete()
    return redirect('products.html')


def calc(request):
    if request.method == 'POST':
        string = str(request.POST['num1'])
        result = 0.0

        # Initialize a variable to store the current number
        current_number = ''
        # Initialize a variable to store the current operation  
        current_operation = '+'
        calculation_steps = []

        for i in string:
            if i == ',':
                i = '.'  # Replace ',' with '.'
            if i.isdigit() or i == '.':
                current_number += i
            elif i in ['+', '-', '*']:
                # If the character is an operator, perform the current operation and update
                if current_operation == '*':
                    result *= round(float(current_number),2)
                elif current_operation == '+':
                    result += round(float(current_number),2)
                elif current_operation == '-':
                    result -= round(float(current_number),2)
                
                calculation_steps.append(f"{current_number} {current_operation}")
                current_number = ''
                current_operation = i

        # Add the last number in the string to the result based on the last operation
        if current_operation == '*':
            result *= round(float(current_number),2)
        elif current_operation == '+':
            result += round(float(current_number),2)
        elif current_operation == '-':
            result -= round(float(current_number),2)

        calculation_steps.append(f"{current_number}")

        content = {
            'result': result,
            'calculation_steps': calculation_steps
        }

        return render(request, 'calculator.html', content)

    return render(request, 'calculator.html')