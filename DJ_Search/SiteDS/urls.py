from django.urls import path
from . import views

urlpatterns = [
     path("home", views.home, name="index"),
     path("imagesearch", views.imagesearch, name="imagesearch"),
     path("advancedsearch", views.advancedsearch, name="advancedsearch"),
]