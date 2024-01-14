# yourapp/tasks.py
from celery import shared_task

@shared_task
def your_celery_task():
    # Your actual task logic goes here
    print("Your Celery task is running!")
