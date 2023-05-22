from django.urls import path

from . import views


app_name = "quotes"
urlpatterns = [
    path("", views.main, name="root"),
    path("<int:page>", views.main, name="root_paginate"),
    path("addauthor", views.add_author, name="addauthor"),
    path("addquote", views.add_quote, name="addquote"),
    path("addtag", views.add_tag, name="addtag"),
    path("details/<str:auth_id>", views.details, name="details"),
    path("quotes_with_tag/<str:tag_name>", views.quotes_with_tag, name="quotes_with_tag"),
    path("popular_tags", views.popular_tags, name="popular_tags")
    
]
