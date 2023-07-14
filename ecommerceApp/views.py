from django.shortcuts import render
from ecommerceApp.models import Contact
from django.contrib import messages

def index(request):
    return render(request,"index.html")

def order(request):
    return render(request,"order.html")

def my_profile(request):
    return render(request,"my_profile.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    if request.method=="POST":
        name=request.POST.get("full_name")
        email=request.POST.get("email")
        desc=request.POST.get("description")
        phone_no=request.POST.get("phone_no" )
        my_query=Contact(name=name,email=email,desc=desc,phone_no=phone_no)
        my_query.save()
        messages.info(request,"We will get back to you soon....")
        return render(request,"contact.html")
    return render(request,"contact.html")

def cart(request):
    return render(request,"cart.html")
