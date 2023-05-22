from pymongo import MongoClient
import configparser

import os
from pathlib import Path

path = Path(__file__)
ROOT_DIR = path.parent.absolute()
config_path = os.path.join(ROOT_DIR, "config.ini")
config = configparser.ConfigParser()
config.read(config_path)

mongo_user = config.get('DB', 'USER')
mongodb_pass = config.get('DB', 'PASSWORD')
db_name = config.get('DB', 'DB_NAME')
domain = config.get('DB', 'DOMAIN')

def get_mongodb():
    path_mongo_db = f"""mongodb+srv://{mongo_user}:{mongodb_pass}@{domain}/{db_name}?retryWrites=true&w=majority"""

    client = MongoClient(path_mongo_db)
    db = client.HW10_1
    return db
