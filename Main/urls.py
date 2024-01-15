from django.urls import path, include
from .views import *

urlpatterns = [
    path('', Index, name='index'),
    path('about/', About, name='about'),
    path('services/', Service, name='services'),
    path('projects/', Project, name='projects'),
    path('project/details/', Project_Detail, name='project-details'),
    path('blogs/', Blogs, name='blogs'),
    path('blogs/full/', BlogsFull, name='blogs'),
    path('contact/', Contact_01, name='contact'),
    path('project/details/', Project_Details, name='project-details'),
    path('add-contact/', Add_Contact, name='add-contact')
]