from django.http import HttpResponse as http
import json

def hello_world(request):
    data = [int(i) for i in request.GET['data'].split(",")]
    sorted_numbers = sorted(data)
    data = {
        'status': 'success',
        'data':sorted_numbers,
        'message': 'Integers sorted succesfully'
    }
    return http(json.dumps(data), content_type="application/json")
