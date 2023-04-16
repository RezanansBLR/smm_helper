from django.urls import path

from .views import index_page, bloger_page

urlpatterns = [
    path("", index_page, name="index"),
    path("analytics/<slug:slug>/", bloger_page, name="bloger"),
]