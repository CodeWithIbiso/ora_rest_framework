# yourapp/tasks.py
from celery import shared_task
from datetime import datetime
from connect.mongo_connect import get_db_handle

@shared_task
def your_celery_task(text="Your Celery task is running!"):
    # Your actual task logic goes here
    current_year = datetime.now().year

    current_year_collection = get_db_handle(f"game_result_times_{current_year}")
    
    print(text)
    return text + "RETURNED"