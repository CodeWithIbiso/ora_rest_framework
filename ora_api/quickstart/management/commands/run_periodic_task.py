# myapp/management/commands/run_periodic_task.py
from django.core.management.base import BaseCommand
from quickstart.tasks import your_celery_task
import time

class Command(BaseCommand):
    help = 'Run a periodic task'

    def handle(self, *args, **options):
        while True:
            # Your logic here
            your_celery_task.apply_async()

            # Sleep for a specified duration (e.g., 60 seconds)
            time.sleep(60)
