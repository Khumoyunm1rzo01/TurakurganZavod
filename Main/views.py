from django.shortcuts import redirect, render
from .models import *
# Create your views here.
import requests

def Index(request):
    slider = Slider.objects.all()
    info = Info.objects.last()
    product = Product.objects.all().order_by('-id')[:6]
    client = Client.objects.all()
    product3 = Product.objects.all().order_by('-id')[:3]
    context = {
        'slider': slider,
        'info': info,
        'product': product,
        'product3': product3,
        'client': client,
    }
    
    return render(request, 'index.html', context)

def About(request):
    about = About_model.objects.last()
    team_members = TeamMember.objects.all()
    client = Client.objects.all()
    info = Info.objects.last()

    context = {
        'about': about,
        'client': client,
        'info': info,
        'team_members': team_members,
    }

    return render(request, 'about.html', context)

def Service(request):
    
    return render(request, 'service.html')

def Project(request):
    
    return render(request, 'project-3-col.html')

def Project_Detail(request):
    
    return render(request, 'projct-details.html')
def Blogs(request):
    
    return render(request, 'blog-sidebar-right.html')

def BlogsFull(request):
    
    return render(request, 'blog-full-width.html')

def Contact(request):
    
    return render(request, 'contact.html')


def Project_Details(request):
    
    return render(request, 'project-details.html')