from bson.objectid import ObjectId

from django import template

from ..utils import get_mongodb

register = template.Library()


def find_author(id_):
    db = get_mongodb()
    author = db.author.find_one({"_id": ObjectId(id_)})
    return author["fullname"]

register.filter('author', find_author)
