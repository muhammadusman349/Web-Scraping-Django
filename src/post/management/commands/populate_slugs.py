from django.core.management.base import BaseCommand
from django.utils.text import slugify
from post.models import Post
from django.db import IntegrityError


class Command(BaseCommand):
    help = 'Populates missing slugs for existing posts'

    def handle(self, *args, **kwargs):
        # Retrieve posts with null or empty slugs
        posts = Post.objects.filter(slug__isnull=True) | Post.objects.filter(slug='')

        if not posts:
            self.stdout.write(self.style.SUCCESS('No posts found with missing slugs.'))
            return

        for post in posts:
            base_slug = slugify(post.title)
            slug = base_slug
            num = 1

            # Ensure slug is unique
            while Post.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{num}"
                num += 1

            post.slug = slug
            try:
                post.save()
                self.stdout.write(self.style.SUCCESS(f'Successfully populated slug for post: {post.title}'))
            except IntegrityError:
                self.stdout.write(self.style.ERROR(f'Failed to save slug for post: {post.title} (IntegrityError)'))
