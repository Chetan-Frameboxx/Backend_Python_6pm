from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, "index.html")
+

def about(request):
    return HttpResponse("Welcome to The About Page.")

def team(request):
    return HttpResponse("Welcome to The Team Page.")

def teamDetails(request, teamid):
    return HttpResponse(teamid)