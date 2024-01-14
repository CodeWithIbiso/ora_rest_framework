# your_app/management/commands/run_timer.py
from django.core.management.base import BaseCommand
from threading import Thread
import time
from datetime import datetime

class TimerThread(Thread):
    def __init__(self, interval, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.interval = interval
        self.daemon = True  # Set the thread as daemon, so it will exit when the main process exits

    def run(self):
        while True:
            # Your timer task logic goes here
            print(f'Timer task executed at {datetime.now()}')

            # Sleep for the specified interval
            time.sleep(self.interval)

class Command(BaseCommand):
    '''
        Rather than this - set time the entire year if time is 87 seconds each that will be the next time

        so we check our current time and see the next time in front of us and how many seconds to reach it

    ''' 
    help = 'Starts the timer automatically when runserver is executed'

    def handle(self, *args, **options):
        pass
        interval = 8  #87 Set the interval in seconds (1.45 minutes)
        timer_thread = TimerThread(interval)
        timer_thread.start()
        self.stdout.write(self.style.SUCCESS('Timer started'))
