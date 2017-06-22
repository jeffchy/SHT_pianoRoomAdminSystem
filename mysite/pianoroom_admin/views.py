from django.http import HttpResponse
from django.shortcuts import render
from .models import Reserve
from django.http import Http404

def index(request):
    timeline = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    # mappers to decode the post str to number
    mapper_start_time = {
        "09:00":0,"09:30":1,"10:00":2,"10:30":3,"11:00":4,"11:30":5,"12:00":6,"12:30":7,"13:00":8,"13:30":9,"14:00":10,"14:30":11,
        "15:00":12,"15:30":13,"16:00":14,"16:30":15,"17:00":16,"17:30":17,"18:00":18,"18:30":19,"19:00":20,"19:30":21,"20:00":22,"20:30":23,
    }
    mapper_duration_time = {
        "0.5 hour":1,"1 hour":1,"1.5 hours":1,"2 hours":1,"2.5 hours":1,"3 hours":1,
    }
    print(request.POST)
    if request.POST:
        print(request.POST['username'])
        print(request.POST['startTime'])
        print(request.POST['durationTime'])



    context = {
        'timeline':timeline,

    }



    return render(request,'pianoroom_admin/index.html',context)
