import os
from datetime import datetime
from pathlib import Path

from mongoengine import *
from mongoengine import EmbeddedDocument, Document
from mongoengine import connect
from mongoengine.fields import BooleanField, DateTimeField, EmbeddedDocumentField, ListField, StringField
import configparser

path = Path(__file__)
ROOT_DIR = path.parent.absolute()
config_path = os.path.join(ROOT_DIR, "config.ini")

config = configparser.ConfigParser()
config.read(config_path)

mongo_user = config.get('DB', 'USER')
mongodb_pass = config.get('DB', 'PASSWORD')
db_name = config.get('DB', 'DB_NAME')
domain = config.get('DB', 'DOMAIN')

mongodb_path = f"""mongodb+srv://{mongo_user}:{mongodb_pass}@{domain}/{db_name}?retryWrites=true&w=majority"""
connect(host=mongodb_path, ssl=True)


class Author(Document):
    fullname = StringField(required=True)
    born_date = DateTimeField()
    born_location = StringField(max_length=500)
    description = StringField()


class Quote(Document):
    tags = ListField(StringField(max_length=300))
    author = ReferenceField(Author, reverse_delete_rule=CASCADE)
    quote = StringField()
    meta = {'allow_inheritance': True}
