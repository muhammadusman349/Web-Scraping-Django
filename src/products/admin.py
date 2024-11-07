from django.contrib import admin
from .models import Product, ProductScrapeEvent
# Register your models here.

admin.site.register(Product)
admin.site.register(ProductScrapeEvent)
