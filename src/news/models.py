from django.db import models

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=2000, default="", unique=True)
    published = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-published']

    def __str__(self):
        return self.title
