from django.urls import path
from .views import display_customers, generate_random_customers

urlpatterns = [
    # path('', home_page, name="scraper"),
    path('generate-customer/', generate_random_customers, name="generate_customers"),
    path('customers-list/', display_customers, name="customers"),
    
]