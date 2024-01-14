from django.apps import AppConfig
from .tasks import your_celery_task
from celery.result import AsyncResult


class QuickstartConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'quickstart' 