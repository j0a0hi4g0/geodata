from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def asia(request):
    return render(request, "asia.html")

