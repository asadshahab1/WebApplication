from django.shortcuts import render
from .models import Visitor
from django.contrib.auth import login,authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
invalid_cred = None
def home_page(request):
    '''
    This function is called when website is opened
    :param request: A view
    :return: Home Page
    '''
    return render(request, "AISite/index.html")
def signUp_page(request):
    """
    This function will be called when user clicks on sign up button to navigate to sign up page. It will act as
    a route to sign up page.
    :param request: A view
    :return: Sign up page
    """
    return render(request,"AISite/signup.html")
def signUp_details(request):
    pass_err = None
    email_err=None
    """
    This function fetches the data of sign up details of user and saves it in the server database.
    :param request: A view
    :return: Sign in page
    """
    first = request.POST["first_name"]
    last = request.POST["last_name"]
    email = request.POST["email"]
    passw = request.POST["password"]
    confirm_pass = request.POST["confirm_password"]
    gender = request.POST["gender"]
    if passw!=confirm_pass and Visitor.objects.filter(username=email).exists():
        return render(request,"AISite/signup.html",{"pass_err":"Passwords do not match","email_err":"Email already taken"})
    elif passw!=confirm_pass:
        return render(request,"AISite/signup.html",{"pass_err":"Passwords do not match"})
    elif Visitor.objects.filter(username=email).exists():
        return render(request, "AISite/signup.html",{"email_err":"Email already taken"})
    else:
        user = Visitor.objects.create_user(username=email, password=passw, first_name=first, last_name=last)
        user.gender = gender
        user.save()
        return HttpResponseRedirect(reverse(signIn_page))
def signIn_page(request):
    '''
    This function will be called when user clicks on sign in button to navigate to sign in page. It will act as a
    route to sign in page.
    :param request: A view
    :return: Sign In page
    '''
    return render(request, "AISite/login.html")

def signIn_details(request):
    '''
    This function is used to authenticate the user
    :param request: A view from which data will be fetched
    :return:
    '''
    email = request.POST["signin_email"]
    password = request.POST["signin_pass"]
    signedin_user = authenticate(request,username=email,password=password)
    if signedin_user is not None:
            login(request,signedin_user)
            return HttpResponseRedirect(reverse(report_gen))
    else:
        return render(request,"AISite/login.html",{'error':"Invalid password or email"})
def report_gen(request):
    '''
    This function is called when report generation page appears
    :param request: A view
    :return: Report generation page
    '''
    return render(request,"AISite/report.html")