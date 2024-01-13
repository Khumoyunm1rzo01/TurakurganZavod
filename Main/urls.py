from django.urls import path, include
from .views import *

urlpatterns = [
    path('', Index, name='index'),
    path('index-dark/', Index_Dark, name='index-dark')
]