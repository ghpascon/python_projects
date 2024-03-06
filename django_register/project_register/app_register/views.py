from django.db import connection
from django.shortcuts import render
from .models import product_info

def home(request):
    return render(request, 'register/home.html')

def save_product(request):
    product_name = request.POST.get('product_name')
    product_color = request.POST.get('product_color')
    product_size = request.POST.get('product_size')
    product_amount = request.POST.get('product_amount')

    existing_product = product_info.objects.filter(product_name=product_name, product_color=product_color, product_size=product_size).first()

    if existing_product:
        existing_product.product_amount += int(product_amount)
        existing_product.save()
    else:
        new_product = product_info(product_name=product_name, product_color=product_color, product_size=product_size, product_amount=product_amount)
        new_product.save()
    return render(request, 'register/home.html')



def register_page(request):
    products = {
    'products': product_info.objects.all()
    }
    return render(request, 'register/product_list.html', products)

def clear_db(request):
    product_info.objects.all().delete()
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='app_register_product_info'")
    return render(request, 'register/clear.html')
