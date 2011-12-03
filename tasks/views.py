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
    tasks = Task.objects.all()
    accepts = request.META['HTTP_ACCEPT_ENCODING']
    if accepts == "text/plain":
        response = "\n".join([task.content for task in tasks])
    elif accepts == "application/json" :
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
    task = Task.objects.create(**request.POST)
    return HttpResponse(json.dumps(task.as_json()), content_type = "application/json")

def update(request, task):
    from cgi import parse_qs
    data = parse_qs(request.raw_post_data)
    print data
    Task.objects.filter(pk = task.id).update(**data)
    task = Task.objects.get(pk = task.id)
    return HttpResponse(json.dumps(task.as_json()), content_type = "application/json")

def destroy(request, task):
    task.delete()
    return HttpResponse()
