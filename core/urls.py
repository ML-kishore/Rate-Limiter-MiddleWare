from django.urls import path,include
from core import views

urlpatterns = [
    path('get_ip/',views.get_ip_address,name='get_ip'),
    path('home/',views.index,name='home'),
]
