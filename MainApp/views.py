from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render

# from .forms import RegisterForm


# Create your views here.
def index(request):
    return HttpResponse("Hello world")

def register(request):
    pass
    # if request.method == 'POST':
    #     # create a form instance and populate it with data from the request:
    #     form = RegisterForm(request.POST)
        
    #     # check whether it's valid:
    #     if form.is_valid():
    #         print("form is valid")
    #         form.save()
    #         return HttpResponseRedirect('/home/')
    #     else:
    #         print("form is not valid")
            

    # if a GET (or any other method) we'll create a blank form
    # else:
    #     print("request is GET")
    #     form = RegisterForm()

    # return render(request, 'student_register.html', {'form': form})


def home(request):
    return HttpResponse("<h1>Home Page</h1>")
def login(request):
    return HttpResponse("<h1>Login Page</h1>")
