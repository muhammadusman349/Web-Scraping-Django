from .models import Customer
from celery import shared_task
from django.core.mail import EmailMessage
from django.utils.crypto import get_random_string
import string
# create your tasks here...! 

@shared_task
def create_multiple_customer(number_of_customer):
    for i in range(number_of_customer):
        name = "customer{}".format(get_random_string(5, string.ascii_letters))
        email = "{}@gmail.com".format(name)
        Customer.objects.create(name=name, email=email)
    return '{} random customer created successfully'.format(number_of_customer) 
