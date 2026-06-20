from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import HeroSection,SpecialHeader, SpecialItem,ServiceSection,Services, FavoriteHeader, FavItem, LatestMenu, Menu, CustomerFeedback, Feedback,Contact,Branches
# Create your views here.

def Homepage(request):
    hero = HeroSection.objects.all()
    special_header = SpecialHeader.objects.all()
    specialitem = SpecialItem.objects.all()
    service_section = ServiceSection.objects.all()
    services = Services.objects.all()
    branches = Branches.objects.all()
    context={
        'hero':hero,
        'special_header' :special_header,
        'specialitem' : specialitem,
        'service_section' :service_section,
        'services': services,
        'branches' : branches
    }
    return render(request,'index.html',context)

def Menupage(request):
    favheader = FavoriteHeader.objects.all()
    favitem = FavItem.objects.all()
    latestmenu = LatestMenu.objects.all()
    menu = Menu.objects.all()
    cusfeedback = CustomerFeedback.objects.all()
    feedback = Feedback.objects.all()
    menu={
        'favheader' : favheader,
        'favitem' : favitem,
        'latestmenu' : latestmenu,
        'menu' : menu,
        'cusfeedback' : cusfeedback,
        'feedback' : feedback
    }
    return render(request, 'menu.html', menu)

def Contactpage(request):
    contact = Contact.objects.all()
    contact={
        'contact' : contact,
    }
    return render(request, 'contact.html', contact)

def ContactReport(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        description = request.POST.get('description')

        Contact.objects.create(
            name = name,
            email = email,
            subject = subject,
            description = description
        )
        return redirect('contactpage')
    return render(request, 'contact.html')

def Reviewpage(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')

        if len(request.FILES) != 0:
            image = request.FILES.get('image')

        Feedback.objects.create(
            name = name,
            image =image,
            description = description
        )
        return redirect('menupage')
    return render(request, 'review.html')

def FeedbackDelete(request, pk):
    feedback = get_object_or_404(Feedback, pk=pk)

    if request.method == 'POST':
        feedback.delete()
        return redirect('menupage')
