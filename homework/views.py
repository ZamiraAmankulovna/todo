from django.shortcuts import render, HttpResponse

# Create your views here.
def homework(request):
    return render(request, "index.html")

def task(request):
    return render(request, 'task.html')

def second(request):
    return HttpResponse('Test2 page')