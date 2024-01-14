from django.apps import AppConfig


class QuickstartConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'quickstart'
    
    def ready(self):
        # Import the management command and execute it when the app is ready
        from quickstart.management.commands import run_timer
        run_timer.Command().handle()