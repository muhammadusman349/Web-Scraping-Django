# src/management/commands/flower.py

from django.core.management.base import BaseCommand
from subprocess import Popen

class Command(BaseCommand):
    help = 'Start Flower for monitoring Celery tasks'

    def handle(self, *args, **kwargs):
        Popen(['celery', '-A', 'conf', 'flower', '--port=5555', '--conf=flowerconfig.py'])
