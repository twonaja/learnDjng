from django.urls import path, re_path
from .views import *


urlpatterns = [
    path('', index, name='main_page'),
    path('names/<slug:car_name>/', names),
    re_path(r'^cars_by_years/(?P<year>[0-9]{4})/', cars_by_years)
]

handler404 = page_not_found