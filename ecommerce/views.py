from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import Product,Order,Customer,category

# Create your views here.
def index(request):
    products=Product.objects.all()
    return render(request,'ecommerce/index.html',{'products':products})
def product(request,pk):
    product=Product.objects.get(id=pk)
    return render(request,'ecommerce/product.html',{'product':product})
def cart_add(request):
    pass

def categories(request,victor):
    #replance hypen with spaces
    victor=victor.replace('-','')
    try:
        categories=category.objects.get(name=victor)
        products=Product.objects.filter(category=categories)
        return render(request,'ecommerce/category.html',{'products':products,'category':categories})

    except:
        messages.success(request,('that categories does not exists'))
        return redirect('/')


def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid details please try again')
            return redirect('login')
    return render(request,'ecommerce/login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name=request.POST['firstname']
        last_name=request.POST['lastname']
        email=request.POST['email']
        password=request.POST['password1']
        password2=request.POST['password2']
        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already taken, use another username')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already used . please use another email')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,password=password,email=email)
                user.save()
                return redirect('login')
        else:
            messages.info("The two password are not a match please reenter the password")
            return redirect('register')
    return render(request,'ecommerce/register.html')
def about(request):
    return render(request,'ecommerce/About.html')
