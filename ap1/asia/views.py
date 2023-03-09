from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def asia(request):
    return render(request, "asia.html")

def cazaquistao(request):
    return render(request, "cazaquistao.html")
def filipinas(request):
    return render(request, "filipinas.html")
def iraque(request):
    return render(request, "iraque.html")
