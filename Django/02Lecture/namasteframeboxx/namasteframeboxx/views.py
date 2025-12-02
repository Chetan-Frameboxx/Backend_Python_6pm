from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, "index.html")

def ticket(request):
    return render(request, "ticket.html")

# def home(request):
#     data= {
#             'title': 'My Website',
#             'greeting': 'Namaste Bharat',
#             'course_list': ['Frontend','Backend','Data Analysis', 'Ui/UX'],
#             'students_details':[
#                 {'name': 'Rohan', 'phone': 1212121212},
#                 {'name': 'Hiren', 'phone': 4545454545}
#             ],
#             'numbers': [10,20,30,40,50]
        
#     }
    
    
#     return render(request, "index.html", data)

def about(request):
    return HttpResponse("Welcome to The About Page.")

def team(request):
    return HttpResponse("Welcome to The Team Page.")

def teamDetails(request, teamid):
    return HttpResponse(teamid)