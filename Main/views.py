from django.shortcuts import redirect, render
from .models import *
# Create your views here.
import requests

def Index(request):
    # title = Title.objects.last()
    # me = Me.objects.last()
    # team = Team.objects.last()
    # about = About.objects.last()
    # design = Design.objects.last()
    # project = Project.objects.last()
    # video = YoutubeVideo.objects.last()
    # context = {
    #     'me': me,
    #     'about': about,
    #     'design': design, 
    #     'title': title,
    #     'video': video,
    #     'project': project, 
    #     'team': team
    # }
    return render(request, 'index.html')

def About(request):
    
    return render(request, 'about.html')

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