from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Customer, Post
from .forms import PostForm
from .tasks import create_multiple_customer
from django.contrib.auth.decorators import login_required
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


def post_home_view(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, "posts/post_home.html", context)


def post_read_view(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {
        'post': post
    }
    return render(request, "posts/post_get.html", context)


@login_required
def post_create_view(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user    
            post.save()
            return redirect('post-home')
    else:
        form = PostForm()

    context = {
        'form': form
    }
    return render(request, "posts/post_create.html", context)


def post_update_view(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect(reverse('post-detail', args=[post.slug]))
    else:
        form = PostForm(instance=post)

    context = {
        'form': form,
        'post': post,  # Ensure 'post' is included in the context
    }
    return render(request, 'posts/post_update.html', context)


def post_delete_view(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        post.delete()
        return redirect('post-home')
    context = {
        'post': post
    }
    return render(request, "posts/post_delete.html", context)
