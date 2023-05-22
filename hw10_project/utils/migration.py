
import os
import django
from pathlib import Path
import configparser

from pymongo import MongoClient



os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hw10_project.settings")
django.setup()

from quotes.models import Quote, Tag, Author
from quotes.utils import get_mongodb

db = get_mongodb()

authors = db.author.find()

for auth in authors:
    Author.objects.get_or_create(
        fullname=auth["fullname"],
        born_date=auth["born_date"],
        born_location=auth["born_location"],
        description=auth["description"]
    )

quotes = db.quote.find()

for q in quotes:
    tags = []
    for tag in q["tags"]:
        t, *_ = Tag.objects.get_or_create(name=tag)
        tags.append(t)

    exist_quote = bool(len(Quote.objects.filter(quote=q["quote"])))

    if not exist_quote:
        author = db.author.find_one({"_id": q["author"]})
        a = Author.objects.get(fullname=author["fullname"])
        quo = Quote.objects.create(
            quote=q["quote"],
            author=a
        )

        for tag in tags:
            quo.tags.add(tag)
    