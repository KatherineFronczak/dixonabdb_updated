from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def database(request):
    return render(request, 'abdb/database.html')
