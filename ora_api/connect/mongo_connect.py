from pymongo import MongoClient
import os # this is for dotenv - recheck

DATABASE_URL = os.getenv('DATABASE_URL')
MONGO_CONFIG_CREDENTIALS = DATABASE_URL


def initial_create_collections_and_db(db_name,collection_names):
    client = MongoClient(MONGO_CONFIG_CREDENTIALS)

    for collection_name in collection_names:
        collection = client[db_name][collection_name]
        collection.insert_one({'key': 'value'})

def drop_all_collections_in_db(db_name,collection_names):
    client = MongoClient(MONGO_CONFIG_CREDENTIALS)

    for collection_name in collection_names:
        client[db_name][collection_name].drop()
    
def get_db_handle():
    client = MongoClient(MONGO_CONFIG_CREDENTIALS)
    db_handle = client['ora']
    
    return db_handle, client

'''
collection_names = [
    'app_result_history',
    'player_transactions', # amount played with this team or ...
    'player_played_history',
    'player_credit_history',
    'player_debit_history',
]
initial_create_collections_and_db('ora',collection_names)
# drop_all_collections_in_db('ora',collection_names)
'''