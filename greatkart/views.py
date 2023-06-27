
# from django.http import render
# from django.http import HttpResponse
from django.shortcuts import render,redirect
from store.models import Product
def home(request):
    products= Product.objects.all().filter(is_available=True)
    print(products)
    context={
        'products':products,
    }
    return render(request, 'home.html',context)