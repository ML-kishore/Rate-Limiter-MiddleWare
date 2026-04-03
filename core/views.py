from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from datetime import timezone
import time
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

#get_ip

usage_data = {}

@api_view(['GET'])
def get_ip_address(request):
    ip_address = request.META.get('REMOTE_ADDR')

    try:
        #debugging Print
        print("Officially in Try")
        if not ip_address:
            return Response({"error" : "Address not Found"},status=404)
    
        if ip_address not in usage_data:
            usage_data[ip_address] = []
        #1.window and limit 
        window_size = 60
        limit = 5
        now = time.time()

        #2.setting usage_data

        # i am trying in traditional loop to visible understanding
        usage_data[ip_address] = [t for t in usage_data[ip_address]if (now - t) < window_size]
        
        #Debugging Prints
        print(usage_data)

        #3.check condition

        if len(usage_data[ip_address]) >= 5:
            return Response({"Limit Exceeded" : f"Try again after {int(window_size - (now - usage_data[ip_address][0]))} seconds"},status=429)
        
        #4.rehit new hit

        usage_data[ip_address].append(now)

        return Response({"status" : f"Request hitted -- remaining - {limit - len(usage_data[ip_address])}"},status=200)
    except Exception as e:
        return Response({"error" : "May be ..."},status=400)
    

#debugging Print

@api_view(['GET'])
@csrf_exempt
def index(request):
    print('View is hitted')
    return Response({"message" : "View hitted"},status=200)

