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

def Index_Dark(request):
    return render(request, 'index-dark.html')
