from django.http import HttpResponse

#RESTful views
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
    return HttpResponse("To view all tasks")

def show(request):
    return HttpResponse("To show a single task")

def create(request):
    return HttpResponse("To create a task")

def update(request):
    return HttpResponse("To update a task")

def destroy(request):
    return HttpResponse("To destroy a task")
