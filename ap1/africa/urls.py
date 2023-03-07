from django.urls import path
from . import views

urlpatterns = [
    path("", views.africa, name="africa"),
    path("", views.angola, name="angola"),


    
]
