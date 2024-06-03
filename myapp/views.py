# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
#from django.shortcuts import get_object_or_404 
from django.shortcuts import render
# Create your views here.
def index(requests):
    titulo = 'Django Curso!!'
    return render(requests, 'index.html', {
        'title' : titulo
    })

def hello(request, username):
    return HttpResponse("<h2>Hello %s</h2>" % username )
def about(requests):
   # return HttpResponse("About")
    usuario = 'Jairo M'
    return render(requests, 'about.html', {
        'autor': usuario
    })

def projects(requests):
    ##projects = list(Project.objects.values())
    #return JsonResponse(projects, safe=False)
    projects = Project.objects.all()
    return render(requests, 'projects.html',{
        'proyectos':projects
    })

#def tasks(requests, id):
def tasks(requests):    
   # task = Task.objects.get(id=id)
   # task = get_object_or_404(Task, id=id)
   # return HttpResponse('task: %s' % task.title)
   tasks = Task.objects.all()
   return render(requests, 'tasks.html',{
       'tareas':tasks
   })

