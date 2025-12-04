from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def home(request):
    return render(request, "index.html")

def ticket(request):
    if request.method == "GET":
        output = request.GET.get('output')
    return render(request, "ticket.html", {'output': output})


def userForm(request):
    result= 0
    try:
        if request.method == "POST":
            n1 = int(request.POST.get("num1"))
            n2 = int(request.POST.get("num2"))
            result = n1 +n2
            data={
                'n1':num1,
                'n2':num2,
                'output':result
            }
            url = '/ticket?output={}'.format(result) 
            return HttpResponseRedirect(url)
    except:
        pass
    return render(request, "userform.html", data)



def contact(request):
    return render(request, "contactus.html")

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