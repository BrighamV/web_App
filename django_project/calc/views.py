from django.views.generic import TemplateView
from django.shortcuts import render
import math
# views for the home and calculate pages
class HomePageView(TemplateView):
    template_name = "home.html"

class CalcPageView(TemplateView):
    template_name = "calculate.html"
# This function is called before getting the answer page
def answer(request):
    num1 = int(request.POST["num1"])
    num2 = int(request.POST["num2"])
    ans = 0
# If statement to find what math operator to use
    if (request.POST["operation"] == "+"):
        print("found +")
        ans = num1 + num2
    elif (request.POST["operation"] == "-"):
        print("found -")
        ans = num1 - num2
    elif (request.POST["operation"] == "x"):
        print("found x")
        ans = num1 * num2
    elif (request.POST["operation"] == "/"):
        print("found /")
        ans = num1 / num2
    elif (request.POST["operation"] == "^"):
        print("found ^")
        ans = num1 ** num2
    else:
        print("found √")
        ans = math.sqrt(num2)
# sending in the data through the django template. The data has to go as a dictionary
    return render(request, "answer.html", {"answer": ans})

def extra(request):
    num1 = int(request.POST["num1"])
    ans = 0
# If statement to find what math operator to use
    if (request.POST["operation"] == "√"):
        print("found √")
        ans = math.sqrt(num1)
    elif(request.POST["operation"] == "cos"):
        print("found cos")
        ans = math.cos(num1)
    elif(request.POST["operation"] == "tan"):
        print("found tan")
        ans = math.tan(num1)
    else:
        print("found sin")
        ans = math.sin(num1)
# sending in the data through the django template. The data has to go as a dictionary
    return render(request, "extra.html", {"answer": ans})



# python manage.py runserver

# source .venv/bin/activate