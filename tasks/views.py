from django.http import HttpResponse
from tasks.models import Task
from django.shortcuts import get_object_or_404
import json

def _collection(request):
    if request.method == 'GET':
        return index(request)
    elif request.method == 'POST':
        return create(request)

def _member(request, task_id):
    task = get_object_or_404(Task, pk = task_id)
    if request.method == 'GET':
        return show(request, task)
    elif request.method == 'PUT':
        return update(request, task)
    elif request.method == 'DELETE':
        return destroy(request, task)

def index(request):
    tasks = Task.objects.all().order_by('-created_at')
    accepts = request.META['HTTP_ACCEPT']
    if accepts == "text/plain":
        response = "\n".join([task.content for task in tasks])
    elif "application/json" in accepts :
        response = json.dumps({
            'tasks': [
                task.as_json()
                for task in tasks
                ]})
    else:
        return HttpResponse(status = 406)
    return HttpResponse(response, content_type = accepts)

def show(request, task):
    return HttpResponse(json.dumps(task.as_json()), content_type = "application/json")

def create(request):
    task = Task()
    task.content = request.POST['content']
    task.save()
    return HttpResponse(json.dumps(task.as_json()), content_type = "application/json")

def update(request, task):
    task.content = request.REQUEST.get('content', [task.content,])[0]
    task.complete = request.REQUEST.get('complete', [task.complete,])[0] == "true"
    task.save()
    return HttpResponse(json.dumps(task.as_json()), content_type = "application/json")

def destroy(request, task):
    task.delete()
    return HttpResponse()
