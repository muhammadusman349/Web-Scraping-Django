from django.shortcuts import render, redirect
from .models import Customer
from .tasks import *
# Create your views here.

def generate_random_customers(request):
    if request.method == "POST":
        num_of_customer = request.POST.get('num_of_customer')
        customers = int(num_of_customer)
        create_multiple_customer.delay(customers)
        return redirect("customers")
    return render(request, "index.html")

def display_customers(request):
    customers = Customer.objects.all()
    context = {
        'customers_list': customers
    }
    return render(request, 'display.html', context)