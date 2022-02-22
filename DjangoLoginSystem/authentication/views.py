from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    if 'login_status' in request.cookies and 'username' in request.cookies:
        context =   {
            'username' : request.cookies['username'],
            'login_status' : request.cookies.get('logged_in'),
        }
        return render(request, 'home.html',context)
    else:
        return render(request, 'home.html')

    # return render(request, 'home.html')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    if request.method == 'POST':
        username = request.POST.get('email')

    response = render(request, 'home.html')

    # Setting Cookies
    response.set_cookie('username', username)
    response.set_cookie('login_status', True)
    return  response

def signup(request):
    return render(request, "authentication/signup.html")


def signin(request):
    return render(request, "authentication/signin.html")


def signout(request):
    pass


def logout(request):
    pass
