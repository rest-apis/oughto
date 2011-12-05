class HttpMethodsMiddleware(object):
    def process_request(self, request):
        if request.method == 'POST' and ('_method' in request.POST):
            request.method = request.POST['_method'].upper()


from cgi import parse_qs
import json

class RestMiddleware(object):
    def process_request(self, request):
        if request.method == 'PUT':
            request.POST = parse_qs(request.raw_post_data)
        if request.META['CONTENT_TYPE'] == 'application/json':
            request.POST = json.loads(request.raw_post_data)


