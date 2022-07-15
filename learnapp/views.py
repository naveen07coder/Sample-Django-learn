from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .forms import *
# Create your views here.
def error_404_view(request,exception):
    return render(request,'404.html')
def myfunctioncall(request):
    return HttpResponse("Hello World!")

def myfunctionabout(request):
    return HttpResponse(" about RESPONSE")

def add(request, a, b):
    return HttpResponse(a+b)

def intro(request, name, age):
    dict = {
        "Name": name,
        "Age" : age
     }
    return JsonResponse(dict)

def firstpage(request):
    return render(request, 'index.html')

def second(request):
    return render(request, 'second.html')

def third(request):
    var = "Hello World@"
    greeting = "Welcome babe!!"
    fruits = ["apple", "Mango", "Orange"]

    num1, num2 = 3, 5
    ans = num1 > num2
    dict = {
        "name": var,
        "Wel": greeting,
        "myfruit": fruits,
        "n1":num1,
        "n2":num2,
        "answer": ans
    }
    return render(request, 'third.html', context=dict)

def ipage(request):
    return render(request, 'ipage.html')

def ipage2(request):
    return render(request, 'ipage2.html')

def ipage3(request):
    return render(request, 'ipage3.html')

def ipage4(request, imagename):
    imagename = str(imagename);
    imagename = imagename.lower();

    if imagename == "django":
        var = True
    elif imagename =="python":
        var = False

    mydic = {
        "var": var
    }
    return render(request, 'ipage4.html', context=mydic)

def forms(request):
    return render(request, 'forms.html')

def sforms(request):

    mydict = {
        "var1": request.GET['mytext'],
        "var2": request.GET['mytext2'],
        "method": request.method
         }
    return JsonResponse(mydict)

def forms2(request):
    if request.method =="POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            title = request.POST['title']
            subject = request.POST['subject']
            email = request.POST['email']
            mydict = {
                "form" : FeedbackForm()
            }
            errorflag = False
            Errors = []
            if title != title.upper():
                errorflag =True
                errormsg = 'Title should be Capital'
                Errors.append(errormsg)
            import re
            regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
            if not re.search(regex, email):
                errorflag = True
                errormsg = 'NOT VALID EMAIL'
                Errors.append(errormsg)
            if errorflag != True:
                mydict["success"] = True
                mydict["successmsg"] = "Form Submitted"
            mydict['error'] = errorflag
            mydict['errors'] = Errors
            print(mydict)
            return render(request, 'forms2.html', context=mydict)


    elif request.method == "GET":
        form = FeedbackForm() # NOne
        mydict = {
            "form": form
        }
        return render(request, "forms2.html", context=mydict)
