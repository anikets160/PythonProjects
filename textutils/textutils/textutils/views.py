from django.http import HttpResponse
from .Dir1 import *
import os.path


def index(request):
    return HttpResponse('''<h1>Welcome to Python Programming using Django Framework and SQLLite database<h1><BR> 
    <a href="https://docs.python.org/3/">Go to Python Official Documentation</a><BR><BR>
    <a href="https://docs.djangoproject.com/en/4.0/">Go to Django Official Documentation</a><BR><BR>
    <a href="https://www.postgresql.org/docs/">Go to PostGresql Official Documentation</a><BR><BR>   
    ''')

def about(request):
    return HttpResponse("<h2>Welcome to About Page<h2>")

def read_file(request):
    f = open('path\one.text', 'r')
    file_content = f.read()
    f.close()
    return HttpResponse(file_content, content_type="text/plain")