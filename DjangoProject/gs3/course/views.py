from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1>HOME PAGE</h1>')

def learn_django(request):
    return HttpResponse('happy learning')