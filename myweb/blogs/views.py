from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def blogs(request):
    return HttpResponse("Welcome blogs ")

def name(request):
    return HttpResponse(" ถิรวัฒน์")