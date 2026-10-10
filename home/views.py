from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello World!")

def about(request):
    return HttpResponse("ABOUT TIME BOI")

def add(request):
    count = request.session.get('count',0)

    if request.method =='POST':
        count+=1
        request.session['count'] = count

    return render(request, 'home/page1.html',{
        'count': count
    })

def home(request):
    name ="Raymundo"
    students = [{
        'name': "Rayy",
        'age': 19,
        'gender': "M"
    },{
        'name': "Munnn",
        'age': 19,
        'gender': "M"
    },{
        'name': "Dowww",
        'age': 19,
        'gender': "M"
    }]
   

    return render(request, 'home/index.html',{
        'name':name, 
        'students':students
    })