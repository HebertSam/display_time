from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
# Create your views here.

def index(request):
    now ={
        'time': strftime('%Y-%m-%d %H:%M %p', gmtime())
    }
    print now['time']
    return render(request,'time_dis/index.html', now)