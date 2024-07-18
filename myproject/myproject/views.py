# from django.http import HttpResponse

# def homepage(request):
#     return HttpResponse("Hello World! I'm Home.")

# def about(request):
#     return HttpResponse("My About Page")

from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')