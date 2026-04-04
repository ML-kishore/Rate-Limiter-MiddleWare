from rest_framework.response import Response
from rest_framework import status
import time
from django.http import JsonResponse
from datetime import timedelta
from django.utils import timezone
from .models import RequestLogs
import math

def rate_limiter_middleware(get_response):

    print('MiddleWare is running .... ✅')
    def wrapper(request):
        print('Rate Limiter Started ....📊')
        ip = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR')
        now = timezone.now()
        window_size =  now - timedelta(minutes=1)
        limit_rate = 5

        #checking if ip is valid
        if not ip:
            return JsonResponse({"message" : "Invalid IP Address"},status=400)

        #1.removing later logs 
        older_requestlogs = RequestLogs.objects.filter(timestamp__lt = window_size).delete()

        #2.counting new logs 

        count_last_window_logs = RequestLogs.objects.filter(
            ip = ip,
            timestamp__gt= window_size
        ).count()

        #3.filtering limit rate

        newer_requests = RequestLogs.objects.filter(ip=ip,timestamp__gt = window_size)
        
        if count_last_window_logs >= limit_rate:
            target_time = newer_requests[0].timestamp
            duration = target_time + timedelta(seconds=60)
            actual_duration = duration - now
            return JsonResponse({"limit_exceeded" : f"Try Again after {int(actual_duration.total_seconds())} seconds"},status=429)
        
        #4.newer requests adding

        RequestLogs.objects.create(ip=ip)

        #5.hitting view

        response = get_response(request)
        return response
    
    return wrapper





        

