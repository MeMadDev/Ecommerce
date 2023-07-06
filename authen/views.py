from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes,force_str
from django.views.generic import View
from .utils import generate_token
from django.core.mail import EmailMessage
from django.conf import settings


def handel_signup(request):
    if request.method=="POST":
        # user_name=request.POST['user_name']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        if password!=confirm_password:
            messages.warning(request,"Password Does Not Match")
            return render(request,"authentication/signup.html")

        try:
            if User.objects.get(username=email):
                # return HttpResponse("Email is Already registered")
                messages.warning(request,"Email is Already registered")
                return render(request,"authentication/signup.html")
        except Exception as identifier:
            pass
        user = User.objects.create_user(email,email,password)
        user.is_active=False
        user.save()
        #For sending the email to verify that user ************************************
        email_subject="Activate Your Account Of Saman LeLo"
        message=render_to_string('authentication/activate.html',{
            'user':user,
            'domain':'127.0.0.1:8000',
            'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            'token':generate_token.make_token(user)
        })

        
        email_message=EmailMessage(
          email_subject,
          message,
          settings.EMAIL_HOST_USER,
          [email]
        )
        email_message.send()
        messages.info(request,'Activate your Account by clicking on the link in your mail')
        return redirect('/auth/login/')
        # return HttpResponse("Account Created succesfully")
    return render(request,"authentication/signup.html")

class ActivateAccountView(View):
    def get(self,request,uidb64,token):
        try:
            uid=force_str(urlsafe_base64_decode(uidb64))
            user=User.objects.get(pk=uid)
        except Exception as identifier:
            user=None
        if user is not None and generate_token.check_token(user,token):
            user.is_active=True
            user.save()
            messages.success(request,'Your Account Activated Sucessfully')
            return redirect ('/')
        return render(request,'authentication/activation_fail.html')

def handel_login(request):
    if request.method=="POST":
        user_name=request.POST['email']
        user_password=request.POST['password']
        myuser=authenticate(username=user_name,password=user_password)

        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login Sucessfully")
            return redirect('/')
        else :
            messages.error(request,"Invalid credentials")
            return redirect('/auth/login')
    return render(request,"authentication/login.html")

def handel_logout(request):
    logout(request)
    messages.info(request,"Sucessfully Logout")
    return redirect('/auth/login')

