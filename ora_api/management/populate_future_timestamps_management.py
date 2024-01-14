from datetime import datetime, timedelta
from pymongo import MongoClient
import os # this is for dotenv - recheck
from dotenv import load_dotenv
# from connect.mongo_connect import get_db_handle

# Load environment variables from .env
load_dotenv()
MONGO_CONFIG_CREDENTIALS = os.getenv('DATABASE_URL')

def generate_time_stamps():
    # we will also need a code to run an hour before end of year to generate for the next year
    current_year = datetime.now().year
    start_date = datetime(current_year, 1, 1, 0, 0, 0)
    end_date = datetime(current_year, 12, 31, 23, 59, 59)
    interval_duration = timedelta(seconds=85)
    
    time_stamps = []
    
    current_date = start_date
    while current_date <= end_date:
        time_stamps.append({"result_time":current_date.strftime("%Y-%m-%d %H:%M:%S"),"combination":""})
        current_date += interval_duration

    # insert to mongodb
    client = MongoClient(MONGO_CONFIG_CREDENTIALS)
    collection = client["ora"][f"game_result_times_{current_year}"]   
    collection.insert_many(time_stamps)
    
    print('Done!')
    return time_stamps

timestamps = generate_time_stamps()
'''
    We need to setup a scheduler to run before end of year and also to run based off time in db
    deactivate (exit)

'''

# import time

# def run_at_timestamp(target_timestamp, func_to_run):
#     current_timestamp = time.time()

#     if current_timestamp >= target_timestamp:
#         print("Target timestamp has already passed.")
#         return

#     sleep_time = target_timestamp - current_timestamp
#     print(f"Sleeping for {sleep_time} seconds until the target timestamp.")

#     time.sleep(sleep_time)

#     # Update the future timestamp to be run (you can modify this based on your needs)
#     new_target_timestamp = target_timestamp + 60  # Example: set the next timestamp to be 1 minute later

#     print(f"Running the function at timestamp {new_target_timestamp}.")
#     run_at_timestamp(time.time() + 10, func_to_run)

#     func_to_run()

# # Example usage:
# def your_function():
#     print("Your function is running!")

# # Set your target timestamp (replace with your desired timestamp)
# target_timestamp = time.time() + 10  # Example: set the target timestamp to be 10 seconds from now

# run_at_timestamp(target_timestamp, your_function)
