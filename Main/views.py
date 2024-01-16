from django.shortcuts import redirect, render
from .models import *
# Create your views here.
import requests
# from django.http import HttpResponse

def Index(request):
    category = Category.objects.all()
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
	'category': category,
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
    bg = Background_Img.objects.last()
    img = Picture.objects.all()
    info = Info.objects.last()
    stats = Statistics.objects.last()
    context = {
        'bg': bg,
        'img': img,
        'stats': stats,
        'info': info,
    }
    return render(request, 'service.html', context)

def Project(request):
    product = Product.objects.all().order_by('-id')
    bg = Background_Img.objects.last()
    info = Info.objects.last()

    context = {
        'bg': bg,
        'product': product,
        'info': info,
    }
    return render(request, 'project-3-col.html', context)

def Project_Detail(request):
    
    return render(request, 'projct-details.html')
def Blogs(request):
    
    return render(request, 'blog-sidebar-right.html')

def BlogsFull(request):
    product = Product.objects.all().order_by('-id')[:6]
    info = Info.objects.last()
    bg = Background_Img.objects.last()

    context = {
        'product': product,
        'bg': bg,
        'info':info
    }
    
    
    return render(request, 'blog-full-width.html', context)

def Contact_01(request):
    bg = Background_Img.objects.last()
    info = Info.objects.last()
    context = {
        'bg': bg,
        'info':info
    }
    return render(request, 'contact.html', context)

# def Contact(request):
    
#     return HttpResponse('Эта страница в настоящее время находится в разработке')

def Project_Details(request):
    
    return render(request, 'project-details.html')

def Add_Contact(request):
    if request.method == "POST":
        name = request.POST['name']
        phone_number = request.POST.get('phone_number')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        Contact.objects.create(name=name, phone_number=phone_number, subject=subject, message=message)
        ids = Telegram_ids.objects.all()
        token = "6403550378:AAF82dSRQIMgy01fnlQuq8FRxAk8zyCnXEo"
        for id in ids:
            text = 'Yangi obuna: \n\nMijoz: ' + name + '\nTelefon raqami: ' + phone_number + '\nMavzu: ' + subject + '\nHabar:' + message
            url = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id='
            requests.get(url + str(id.ids) + '&text=' + text)
    return redirect('index')
            

def Programmers_View(request):
    programmers = Programmer.objects.all()
    client = Client2.objects.all()
    info = Info.objects.last()
    context = {
        'programmers': programmers,
        'client': client,
        'info':info,
    }
    return render(request, 'programmers.html', context)
