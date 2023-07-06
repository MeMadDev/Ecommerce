from django.shortcuts import render

def index(request):
    return render(request,"index.html")

def order(request):
    return render(request,"order.html")

def my_profile(request):
    return render(request,"my_profile.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def cart(request):
    return render(request,"cart.html")
