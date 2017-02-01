from django.http import HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from .forms import *


# Create your views here.


def index(request):
    """
    The Base view of the website, i.e. at url '/' This view will be called
    :param request: The HTTP request
    :return: render the index template populated with the models data
    """
    events = Events.objects.all()
    achievement=Achievements.objects.all()
    news=News.objects.all()
    direc=ddesk.objects.get(pk=1)
    init=initiatives.objects.all()
    return render(request, 'index.html', {
        'events': events,
        'achievement':achievement,
        'news': news,
        'description':direc.description,
        'init': init,
    })


def add_event(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/')
    else:
        eventForm = EventForm()
        return render(request, 'add.html', {
            'eventForm': eventForm,
        })

def add_achievement(request):
    if request.method == "POST":
        form=AchievementForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return  HttpResponseRedirect('/')
    else:
        achievementForm=AchievementForm()
        return render(request,'add_achievement.html',{'form':achievementForm})

def add_news(request):
    if request.method == "POST":
        form=NForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return  HttpResponseRedirect('/')
    else:
        NewsForm=NForm()
        return render(request,'add_news.html',{'form':NewsForm})

def cddesk(request):
    if request.method == "POST":
        instance = get_object_or_404(ddesk, pk=1)
        form = ddeskForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form=ddeskForm()
        return render(request, 'changedd.html', {'form': form})


def add_initiative(request):
    if request.method == "POST":
        form=IForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return  HttpResponseRedirect('/')
    else:
        form=IForm()
        return render(request,'add_initiative.html',{'form':form})