class HttpMethodsMiddleware(object):
    def process_request(self, request):
        if request.method == 'POST' and ('_method' in request.POST):
            request.method = request.POST['_method'].upper()
