from django.urls import path,include
from core import views

urlpatterns = [
    path('home/',views.index,name='home'),
]
