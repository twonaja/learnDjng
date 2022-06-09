from django.urls import path
from .views import *


urlpatterns = [
    path('', index),
    path('names/<slug:car_name>/', names),
]
