from datetime import timedelta

BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

CELERYBEAT_SCHEDULE = {
    'run-every-hour': {
        'task': 'your_app.tasks.your_periodic_task',
        'schedule': timedelta(hours=1),
    },
}
