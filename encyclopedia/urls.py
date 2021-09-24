from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("q/", views.search, name="q"),
    path("wiki/<slug>/", views.single_entry, name="single-entry")
]
