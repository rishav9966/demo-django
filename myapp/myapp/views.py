from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.base import RedirectView

class Gothrough(RedirectView):
    url = "https://facebook.com"

def index(request):
    return HttpResponse("<h1>Hello this is the index of the project</h1>")

def my_app(request):
    return redirect('/myapp')


#  infinite loops through redircet
def inf1(request):
    return redirect('/inf2')
def inf2(request):
    return redirect('/inf1')
#  infinite loops through redircet

def setcookie(request):
    html = HttpResponse("<h1>Django basic app</h1>"+str(request.COOKIES.get('visits')))
    if request.COOKIES.get('visits'):
        html.set_cookie('app', 'Welcome Back')
        value = int(request.COOKIES.get('visits'))
        html.set_cookie('visits', value + 1)
    else:
        value = 1
        text = "Welcome to the django basic app"
        html.set_cookie('visits', value)
        html.set_cookie('app', text)
    return html

def getcookie(request):
    if request.COOKIES.get('visits') is not None:
        value = request.COOKIES.get('visits')
        text = request.COOKIES.get('app')
        html = HttpResponse("<center><h1>{0}<br>You have visited this page {1} times</h1></center>".format(text, value))
        html.set_cookie('visits', int(value) + 1)
        return html
    else:
        return redirect('/setcookie')

def delcookie(request):
    if request.COOKIES.get('visits'):
        response = HttpResponse("<h1>App<br>Cookie deleted</h1>")
        response.delete_cookie('visits')
    else:
        response = HttpResponse("<h1>App</h1> need to be created before deleting")
    return response

# checking cookies on browser
def cookie_session(request):
    request.session.set_test_cookie()
    return HttpResponse("<h1>My app</h1>")
def cookie_delete(request):
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        response = HttpResponse("<h1>App</h1><br>cookie created")
    else:
        response = HttpResponse("<h1>App</h1><br>Your browser doesn't support cookies")
    return response

# adding code for session
def create_session(request):
    request.session['name'] = 'username'
    request.session['password'] = 'password123'
    return HttpResponse("<h1>App</h1><br>the session is set0<br>can be accessed now")

def access_session(request):
    response = "<h1>Welcome to session of App</h1><br>"
    if request.session.get('name'):
        response+="Name : {0} <br>".format(request.session.get('name'))
    if request.session.get('password'):
        response+="Password : {0} <br>".format(request.session.get('password'))
        return HttpResponse(response)
    else:
        return redirect('../create/')
def del_session(request):
    try:
        del request.session['name']
        del request.session['password']
    except KeyError:
        pass
    return HttpResponse("<h1>App</h1><br>Session data cleared")