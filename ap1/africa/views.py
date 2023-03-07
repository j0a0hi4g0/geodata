from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def africa(request):
    return render(request, "africa.html")
def angola(request):
    return render(request, "angola.html")


