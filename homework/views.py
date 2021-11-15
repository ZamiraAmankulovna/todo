from django.shortcuts import render, HttpResponse
from .models import ToDo

# Create your views here.
def homework(request):
    return render(request, "index.html")

def task(request):
    todo_list = ToDo.objects.all()
    return render(request, 'task.html', {"todo_list": todo_list})

def second(request):
    return HttpResponse('Test2 page')