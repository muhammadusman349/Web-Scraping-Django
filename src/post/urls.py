from django.urls import path
from .views import (display_customers, generate_random_customers, 
                    post_read_view, post_create_view, 
                    post_delete_view, post_home_view, post_update_view)

urlpatterns = [
    # path('', home_page, name="scraper"),
    path('generate-customer/', generate_random_customers, name="generate_customers"),
    path('customers-list/', display_customers, name="customers"),
    path('posts/home/', post_home_view, name='post-home'),
    path('posts/<slug:slug>/', post_read_view, name='post-detail'),
    path('post/create/', post_create_view, name='post-create'),
    path('post/<slug:slug>/edit/', post_update_view, name='post-update'),
    path('posts/<slug:slug>/delete/', post_delete_view, name='post-delete'),
    
]