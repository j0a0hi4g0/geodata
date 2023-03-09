from django.urls import path
from . import views

urlpatterns = [
    path("", views.africa, name="africa"),
    path("angola", views.angola, name="angola"),
    path("egito", views.egito, name="egito")
   
]
