from django.db import models
from django.db.models import Max
from django.urls import reverse
from django.utils.text import slugify
from account.models import User
# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150, unique=True)
    
    def __str__(self):
        return self.name


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, unique=True,  blank=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at', '-updated_at']
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            last_slug = Post.objects.filter(
                slug__startswith=base_slug).aggregate(Max('slug'))['slug__max']
            if last_slug:
                parts = last_slug.rsplit('-', 1)
                num = int(parts[-1]) + 1 if parts[-1].isdigit() else 1
                self.slug = f"{base_slug}-{num}"
            else:
                self.slug = base_slug
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post-detail", args=[str(self.slug)])
