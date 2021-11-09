from django.shortcuts import render, HttpResponse

# Create your views here.
def homework(reguest):
    return HttpResponse('добро пожаловать в приложение ToDo - Admin')

def task(reguest):
    return render(reguest, 'task.html')

def second(request):
    return HttpResponse('Test2 page')