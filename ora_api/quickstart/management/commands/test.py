# # yourapp/management/commands/run_periodic_task.py
# from django.core.management.base import BaseCommand
# from time import sleep
# from quickstart.tasks import your_celery_task  # Import your Celery task

# class Command(BaseCommand):
#     help = 'Run a periodic task'

#     def handle(self, *args, **options):
#         while True:
#             # Your logic here
#             your_celery_task.delay()  # Delay execution using Celery task
#             self.stdout.write(self.style.SUCCESS('Task executed. Sleeping for 60 seconds.'))
#             sleep(60)  # Sleep for 60 seconds before the next iteration


# run using python manage.py test.py