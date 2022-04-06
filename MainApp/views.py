from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render

from .forms import *
from .models import *


# Create your views here.
def index(request):
    return HttpResponse("Hello world")

def register(request):
    # pass
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        
        # check whether it's valid:
        if form.is_valid():
            print("form is valid")
            form.save()
            return redirect("login")
        else:
            print("form is not valid")
            for errors in form.errors:
                print(errors)
            return render(request, 'student_register.html', {'form': form})

    # if a GET (or any other method) we'll create a blank form
    else:
        print("request is GET")
        form = RegisterForm()

    return render(request, 'student_register.html', {'form': form})





def loginpage(request):

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        print(email, password)
        user = authenticate(request, username=email, password=password)
        print(user)
        print(type(user))
        if user is not None:
            # print("User Id:", user.id)
            print("User Name:", user.name)
            login(request, user)
            return redirect("home")
         
        else:
            messages.info(request, "Email or Password is Incorrect")
    return render(request, "login.html", {})

@login_required(login_url='login')
def logoutpage(request):
    logout(request)
    return redirect("login")

@login_required(login_url='login')
def home(request):
    product_list = Product.objects.all()
    print(product_list)
    return render(request, 'home.html', {'product_list': product_list})

@login_required(login_url='login')
def profile(request):
    return render(request, "profile.html", {})

@login_required(login_url='login')
def add_product(request):
    form = ProductForm()
    # print(form)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.owner = request.user
            print(request.user)
            product.save()
            return redirect("home")
        else:
            print("form is not valid")
            for errors in form.errors:
                print(errors)
            return render(request, 'add_product.html', {'form': form})
    return render(request, "add_product.html", {'form': form})

def view_product(request, id):
    product = Product.objects.get(id=id)
    comments = Comment.objects.filter(product=product)
    print(comments)
    return render(request, "view_product.html", {'product': product, 'comments': comments})
