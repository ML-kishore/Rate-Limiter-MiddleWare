from rest_framework.response import Response
from rest_framework import status
import time
from django.http import JsonResponse


usage_data = {}

def rate_limiter_middleware(get_response):
    
    print('Middleware is Running.... ✅')
    def wrapper(request):
        print('Rate limiter started .... 📊')
        ip = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR')
        if not ip:
            return JsonResponse({"message" : "IP ADDRESS NOT VALID"},status=400)
        
        response = get_response(request)
        if hasattr(response, 'render') and callable(response.render):
            response.render()
        print(f"IP ADDRESS : {ip}")

        now = time.time()
        #1.initializing usage_data
        if ip not in usage_data:
            usage_data[ip] = []

        window_size = 60
        limit = 5

        #2.appending request hitting time

        usage_data[ip] = [t for t in usage_data[ip] if (now - t) < window_size ]

        #3.checking the valid length

        if len(usage_data[ip]) >= 5:
            return JsonResponse({"limit_exceeded" : f"Try again after sometime {int((window_size) - (now - usage_data[ip][0]))} seconds"},status=429)
        
        
        
        usage_data[ip].append(now)

        response = get_response(request)
        if hasattr(response, 'render') and callable(response.render):
            response.render()

        return response
    
    return wrapper
        


        

