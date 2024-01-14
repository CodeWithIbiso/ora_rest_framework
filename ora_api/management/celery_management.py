import subprocess
import time

import os

# Get the absolute path of the directory containing this script
script_directory = os.path.dirname(os.path.abspath(__file__))

# Change to the directory where celery is located (assuming it's one folder down)
ora_api_directory = os.path.join(script_directory, '..')
os.chdir(ora_api_directory)

def stop_redis_server():
    try:
        subprocess.run(["redis-cli", "shutdown"])
        print("Redis server stopped successfully.")
    except Exception as e:
        print(f"Error stopping Redis server: {e}")

def stop_celery_worker():
    try:
        subprocess.run(["pkill", "-f", "celery worker"])
        print("Celery worker stopped successfully.")
    except Exception as e:
        print(f"Error stopping Celery worker: {e}")

def stop_celery_beat():
    try:
        subprocess.run(["pkill", "-f", "celery beat"])
        print("Celery Beat stopped successfully.")
    except Exception as e:
        print(f"Error stopping Celery Beat: {e}")

def start_redis_server():
    try:
        subprocess.Popen(["redis-server"])
        print("Redis server started successfully.")
    except Exception as e:
        print(f"Error starting Redis server: {e}")

def run_celery_worker_and_beat():
    # Stop Redis server, Celery worker, and Celery Beat if running
    stop_redis_server()
    stop_celery_worker()
    stop_celery_beat()

    # Allow some time for the previous processes to stop (adjust as needed)
    time.sleep(2)

    # Start Redis server
    start_redis_server()

    # Allow some time for Redis to start (adjust as needed)
    time.sleep(2)

    # Start Celery worker
    worker_command = "celery -A ora_api worker --loglevel=info"
    worker_process = subprocess.Popen(worker_command, shell=True)

    # Start Celery Beat
    beat_command = "celery -A ora_api beat --loglevel=info"
    beat_process = subprocess.Popen(beat_command, shell=True)

    # Wait for the worker process to finish
    worker_process.wait()

    # Note: Celery Beat runs continuously in the background, so no need to wait for it to finish

# Call the function to stop existing Redis server, Celery worker, and Celery Beat,
# then start a new Redis server, run the Celery worker, and start Celery Beat
run_celery_worker_and_beat()