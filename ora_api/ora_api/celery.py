# ora_api/celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ora_api.settings')

# create a Celery instance and configure it.
app = Celery('ora_api')

# Load task modules from all registered Django app configs.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Auto-discover tasks in all installed apps
app.autodiscover_tasks()

# # Set broker_connection_retry_on_startup to True
# app.conf.broker_connection_retry_on_startup = True

# =============================================== FOR BEAT SCHEDULER

# Additional Celery Beat configuration
from datetime import timedelta
app.conf.beat_schedule = {
    'run-every-hour': {
        'task': 'quickstart.tasks.your_celery_task',
        'schedule': timedelta(seconds=2), #hours=2,seconds=2,days=1,minutes=1
    },
}