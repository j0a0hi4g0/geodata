from django.urls import path
from . import views

urlpatterns = [
    path("", views.asia, name="asia"),
    path("cazaquistao", views.cazaquistao, name="cazaquistao"),
    path("filipinas", views.filipinas, name="filipinas"),
    path("iraque", views.iraque, name="iraque"),

]
