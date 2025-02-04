from django.http import JsonResponse

class IPAuthenticationMiddleware:
    ALLOWED_IPS = ['180.83.78.96']

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        client_ip = request.META.get('REMOTE_ADDR')
        if client_ip not in self.ALLOWED_IPS:
            return JsonResponse({'error': 'Forbidden: Unauthorized IP address'}, status=403)

        response = self.get_response(request)
        return response
