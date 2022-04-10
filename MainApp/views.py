from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render

from .forms import *
from .models import *

# Create your views here.


def register(request):
    # pass
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST, request.FILES)
        
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
        # print("request is GET")
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
    product_list = Product.objects.all().order_by('-created_at')
    catagories = Catagory.objects.all()
    if request.method == 'POST':
        catagory_selected = request.POST.get("catagory")
        status_selected = request.POST.get("status")
        negotiable_selected = request.POST.get("negotiable")
        print(negotiable_selected)
        print(status_selected)
        min_price_selected = request.POST.get("min_price")
        max_price_selected = request.POST.get("max_price")

        # print(catagory_selected)
        product_list = Product.objects.filter(catagory=catagory_selected, negotiable = negotiable_selected, status = status_selected, price__lte = max_price_selected, price__gte = min_price_selected).order_by('-created_at')
        # product_list = Product.objects.filter(catagory=catagory).order_by('-created_at')
        return render(request, 'home.html', {'product_list': product_list, 'catagories': catagories})
    return render(request, 'home.html', {'product_list': product_list, 'catagories': catagories})

@login_required(login_url='login')
def profile(request, sid):
    user = CustomUser.objects.get(sid=sid)
    if request.user != user:
        return redirect("home")
    products = Product.objects.filter(owner=user)
    reviews = Review.objects.filter(seller=user)
    return render(request, "profile.html", {'user': user, 'products': products, 'reviews': reviews})

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

@login_required(login_url='login')
def view_product(request, id):
    product = Product.objects.get(id=id)
    comments = Comment.objects.filter(product=product)
    # print(comments)
    return render(request, "view_product.html", {'product': product, 'comments': comments})

@login_required(login_url='login')
def comment(request):
    if request.method == "POST":
        product_id = request.POST.get("product_id")

        comment = request.POST.get("comment")

        product = Product.objects.get(id=product_id)
      
        comment = Comment(text=comment, product=product, commenter = request.user)
        comment.save()
        return redirect("view_product", id=product_id)
    return render(request, "view_product.html", {'product': product})


@login_required(login_url='login')
def seller(request, sid):
    seller = CustomUser.objects.get(sid=sid)
    products = Product.objects.filter(owner=seller)
    reviews = Review.objects.filter(seller=seller)
    return render(request, "seller.html", {'seller': seller, 'products': products, 'reviews': reviews})

@login_required(login_url='login')
def delete_product(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('profile', sid=request.user.sid)
@login_required(login_url='login')
def edit_product(request, id):

    product = Product.objects.get(id=id)
    if product.owner != request.user:
        return redirect("home")
    form = ProductForm(instance=product)
    print(form)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
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
            return render(request, 'edit_product.html', {'form': form})
    return render(request, "edit_product.html", {'form': form})


@login_required(login_url='login')
def edit_profile(request, sid):
    user = CustomUser.objects.get(sid=sid)
    if request.user != user:
        return redirect("home")
    form = RegisterForm(instance=user)
    print(form)
    if request.method == "POST":
        form = RegisterForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect("profile", sid=sid)
        else:
            print("form is not valid")
            for errors in form.errors:
                print(errors)
            return render(request, 'edit_profile.html', {'form': form})
    return render(request, "edit_profile.html", {'form': form})
