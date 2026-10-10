from django.shortcuts import render


def hello(request):
    return HttpResponse("Hello World!")