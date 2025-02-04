from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

def test_endpoint(request):
    return JsonResponse({'message': 'This is a test endpoint!'})

@api_view(['GET'])
def hello_world(request):
    return Response({
        "message": "Hello, World!",
        "status": "success"
    })
