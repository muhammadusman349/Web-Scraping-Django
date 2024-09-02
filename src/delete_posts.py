
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "conf.settings")
import django
django.setup()
from post.models import Post

posts = Post.objects.all()
for post in posts:
    post.delete()
