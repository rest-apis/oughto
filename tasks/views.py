from django.http import HttpResponse
from tasks.models import Task
import json

def _collection(request):
    if request.method == 'GET':
        return index(request)
    elif request.method == 'POST':
        return create(request)

def _member(request, task_id):
    #TODO: do something with the task_id
    if request.method == 'GET':
        return show(request)
    elif request.method == 'PUT':
        return update(request)
    elif request.method == 'DELETE':
        return destroy(request)

def index(request):
    tasks = Task.objects.all()
    accepts = request.META['HTTP_ACCEPT_ENCODING']
    if accepts == "text/plain":
        response = "\n".join([task.content for task in tasks])
    elif accepts == "application/json" :
        response = json.dumps({
            'tasks': [
                dict(content = task.content, complete = task.complete, created= str(task.created_at))
                for task in tasks
                ]})
    else:
        return HttpResponse(status = 406)
    return HttpResponse(response, content_type = accepts)

def show(request):
    return HttpResponse("To show a single task")

def create(request):
    return HttpResponse("To create a task")

def update(request):
    return HttpResponse("To update a task")

def destroy(request):
    return HttpResponse("To destroy a task")
