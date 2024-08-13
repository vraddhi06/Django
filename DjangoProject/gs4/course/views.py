from django.shortcuts import render,HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('Home page')

def learn_django(request):
    return HttpResponse('Hello django')

def learn_python(request):
    return HttpResponse('python')

def learn_var(request):
    a='<h1>Hello everyone</h1>'
    return HttpResponse(a)

def learn_math(request):
    a=10+10
    return HttpResponse(a)

def learn_format(request):
    a='good'
    return HttpResponse(f'she is a {a} girl')