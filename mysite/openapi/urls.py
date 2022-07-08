from django.urls import path

from .views import *

app_name = 'openapi'

urlpatterns = [
    path('', index, name='index'),
]