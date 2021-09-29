from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<slug>/", views.single_entry, name="single-entry"),
    path("search/q=<q>/", views.search, name="search"),
    path("new", views.new_entry, name="new-entry"),
    path("wiki/<slug>/edit/", views.edit_entry, name="edit-entry"),
    path("random/", views.random, name="random")
]
