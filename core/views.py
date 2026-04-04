from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from datetime import timezone
import time
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

    

#debugging Print

@api_view(['GET'])
@csrf_exempt
def index(request):
    print('View is hitted')
    return Response({"message" : "View hitted"},status=200)

