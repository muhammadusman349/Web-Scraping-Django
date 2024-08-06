from celery import shared_task
import logging

logger = logging.getLogger(__name__)

@shared_task
def log_message():
    logger.info("Task is running every 30 seconds")
    return "Task is running"

@shared_task
def add(x, y):
    return x + y