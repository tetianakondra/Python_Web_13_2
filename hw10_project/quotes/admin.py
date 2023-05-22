from django.contrib import admin
from .models import Author, Quote, Tag

# Register your models here.
admin.site.register(Author)
admin.site.register(Quote)
admin.site.register(Tag)
