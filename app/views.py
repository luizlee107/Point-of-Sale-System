from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from django.http import JsonResponse
import json
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.db.models import Q



def products_filter(request):
    # Handling GET requests
    if request.method == 'GET':
        name_to_filter = request.GET.get('name') 
        barcode_to_filter = request.GET.get('barcode')
        
        if name_to_filter:
            products = Product.objects.filter(name__icontains=name_to_filter) 
        elif barcode_to_filter:
            products = Product.objects.filter(barcode__icontains=barcode_to_filter) 
        else:
            products = Product.objects.all()
            
            
    context = {    
        'products': products
    }
        
    return render(request, 'products_filter.html', context)

def pos(request):
    cart_items = []  # Default value
    cart_total = 0

    if request.method == 'GET':
        search = request.GET.get('name')
       
        if search:
            filtered_products = Product.objects.filter(Q(name__icontains=search) | Q(barcode__icontains=search))
            for product in filtered_products:
                print("Processing product:", product.name, "Barcode:", product.barcode)  # Debugging line
                if product.barcode:  # Check if barcode is not empty
                    cart_entry, created = Cart.objects.get_or_create(product=product)
                    
                    if not created:
                        cart_entry.quantity += 1
                        cart_entry.save()
        else:
            filtered_products = Product.objects.all()

        cart_items = Cart.objects.all()
  

        for cart_item in cart_items:
       
            cart_item.subtotal = cart_item.quantity * cart_item.product.price
            cart_total += cart_item.subtotal
            

    context = {
        'filtered_products': filtered_products,
        'cart_items': cart_items,
        'cart_total': cart_total,
    }

    return render(request, 'pos.html', context)


def cash(request):
    cart_total = Cart(product)
    
    return render(request, 'cash.html', {'cart_total': cart_total})

def card(request):
    cart_total = Cart(product)
    
    return render(request, 'card.html', {'cart_total': cart_total})


def delete_cart(request, pk=None):
    cart = get_object_or_404(Cart, product_id=pk)
    cart.delete()
    return redirect('pos')

def delete_cart_all(request):
    Cart.objects.all().delete()  
    return redirect('pos')
      



def product(request):
     # Handling GET requests
    if request.method == 'GET':
        name_to_filter = request.GET.get('name') 
        barcode_to_filter = request.GET.get('barcode')
        
        if name_to_filter:
            products = Product.objects.filter(name__icontains=name_to_filter) 
        elif barcode_to_filter:
            products = Product.objects.filter(barcode__icontains=barcode_to_filter) 
        else:
            products = Product.objects.all()
            
    context = {    
        'products': products
    }
        
    return render(request, 'product.html', context)


def product_list(request):
    return render(request, 'product_list.html', {
        'products': Product.objects.all(),
    })


def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "productListChanged": None,
                        "showMessage": f"{product.name} added."
                    })
                })
    else:
        form = ProductForm()
    return render(request, 'product_form.html', {
        'form': form,
    })


def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "productListChanged": None,
                        "showMessage": f"{product.name} updated."
                    })
                }
            )
    else:
        form = ProductForm(instance=product)
    return render(request, 'product_form.html', {
        'form': form,
        'product': product,
    })


#@ require_POST
def remove_product(request, pk=None):
    product = get_object_or_404(Product, id=pk)
    product.delete()
    return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "productListChanged": None,
                "showMessage": f"{product.name} deleted."
            })
        })




def calc(request):
    if request.method == 'POST':
        string = str(request.POST['num1'])
        result = 0.00

        # Initialize a variable to store the current number
        current_number = ''
        # Initialize a variable to store the current operation  
        current_operation = '+'
        calculation_steps = []

        for i in string:
            if i == ',':
                i = '.'  
            if i.isdigit() or i == '.':
                current_number += i
            elif i in ['+', '-', '*']:
                
                if current_operation == '*':
                    result *= float(current_number)
                elif current_operation == '+':
                    result += float(current_number)
                elif current_operation == '-':
                    result -= float(current_number)
                
                # Use string formatting to ensure exactly two decimal places
                calculation_steps.append(f" {float(current_number):.2f} {current_operation}")
                current_number = ''
                current_operation = i

        # Add the last number in the string to the result based on the last operation
        if current_operation == '*':
            result *= float(current_number)
        elif current_operation == '+':
            result += float(current_number)
        elif current_operation == '-':
            result -= float(current_number)

        # Use string formatting to ensure exactly two decimal places
        calculation_steps.append(f"{float(current_number):.2f}")

        content = {
            'result': f"{result:.2f}",
            'calculation_steps': calculation_steps
        }

        return render(request, 'calculator.html', content)

    return render(request, 'calculator.html')


"""
def pos(request):
    # Initialize variables

    cart_total = 0
    form = PosForm(request.POST or None)
    products = Product.objects.all()
    cart_items=Cart.objects.all()  

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('product_list')
        
        # Process form data here if needed
        
    # Populate cart_items with all filtered products
    for item in cart_items:
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
"""