'''
    celery every second to check if the time matches. if it does then
    run the program

    redis-cli shutdown
'''
'''
    To run Celery and process tasks, you need to start a Celery worker process. In your project directory, 
    run the following command:

    redis-server
    celery -A ora_api worker --loglevel=info
    celery -A ora_api beat --loglevel=info
'''
'''
    def ready(self):
        # Import the management command and execute it when the app is ready
        # from quickstart.management.commands import run_timer
        if not getattr(self, 'script_executed', False):
            from management.celery_management import run_celery_worker
            run_celery_worker()
            self.script_executed = True
'''
