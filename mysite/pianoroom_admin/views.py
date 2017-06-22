from django.http import HttpResponse
from django.shortcuts import render
from .models import Reserve
from django.http import Http404

# mappers to decode the post str to number
mapper_start_time = {
    "09:00":0,"09:30":1,"10:00":2,"10:30":3,"11:00":4,"11:30":5,"12:00":6,"12:30":7,"13:00":8,"13:30":9,"14:00":10,"14:30":11,
    "15:00":12,"15:30":13,"16:00":14,"16:30":15,"17:00":16,"17:30":17,"18:00":18,"18:30":19,"19:00":20,"19:30":21,"20:00":22,"20:30":23,
}
mapper_duration_time = {
    "0.5 hour":1,"1 hour":2,"1.5 hours":3,"2 hours":4,"2.5 hours":5,"3 hours":6,
}

list_time = ["09:00","09:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30","14:00","14:30","15:00","15:30",\
"16:00","16:30","17:00","17:30","18:00","18:30","19:00","19:30","20:00","20:30","21:00"]


def initTimeLine(timeline):
    # get all the beckend object and parse it
    reserver_set = Reserve.objects.all()
    print(reserver_set,len(reserver_set))

    for i in reserver_set:

        for t in range(i.start_time,i.end_time):
            timeline[t][0] = 1
            timeline[t][1] = i.reserver_name
            timeline[t][2] = list_time[i.start_time]
            timeline[t][3] = list_time[i.end_time]
    print("after query",timeline)
    return timeline

def updateTimeLine(timeline,start_time,end_time,username):
    for i in range(start_time,end_time):
        timeline[i][0] = 1
        timeline[i][1] = username
        timeline[i][2] = list_time[start_time]
        timeline[i][3] = list_time[end_time]
    print("updated timeline",timeline)
    return timeline

def index(request):
    # init the timeline
    # [isOccupied,username,starttime,endtime]
    timeline = [[0,'','','',"09:00"],[0,'','','',"09:30"],[0,'','','',"10:00"],[0,'','','',"10:30"],[0,'','','',"11:00"],\
    [0,'','','',"11:30"],[0,'','','',"12:00"],[0,'','','',"12:30"],[0,'','','',"13:00"],[0,'','','',"13:30"],\
    [0,'','','',"14:00"],[0,'','','',"14:30"],[0,'','','',"15:00"],[0,'','','',"15:30"],[0,'','','',"16:00"],\
    [0,'','','',"16:30"],[0,'','','',"17:00"],[0,'','','',"17:30"],[0,'','','',"18:00"],[0,'','','',"18:30"],\
    [0,'','','',"19:00"],[0,'','','',"19:30"],[0,'','','',"20:00"],[0,'','','',"20:30"]]

    # read the current state timeline
    timeline = initTimeLine(timeline)

    print(request.POST)
    if request.POST:
        print(request.POST['username'])
        print(request.POST['startTime'])
        print(request.POST['durationTime'])

        try:
            start_time = mapper_start_time[request.POST['startTime']]
        except KeyError:
            raise Http404("invalid time")

        duration_time = mapper_duration_time[request.POST['durationTime']]
        end_time = start_time + duration_time
        if end_time > 24:end_time = 24 # prevent the index error
        username = request.POST['username']
        message = ""
        isOccupied = 0
        # check if has been occupied
        for i in range(start_time,end_time):
            if timeline[i][0] == 1:
                print('occupied')
                message = "Time conflict, someone already in there!"
                isOccupied = 1
                status = 2 # occupied
                break

        # if it is not occupied we can save it
        if not isOccupied:
            timeline = updateTimeLine(timeline,start_time,end_time,username)
            # save it
            new_reserve = Reserve(reserver_name=username,use_text='temp',start_time=start_time,end_time=end_time)
            new_reserve.save()
            status = 1 # 1 is the not Occupied
            message = "Piano Room Reserved Successfully!"

        context = {
            'timeline':timeline,
            'message':message,
            'status':status,
        }
        return render(request,'pianoroom_admin/index.html',context)

    else:
        # not a post represt
        message = "Welcome, click and reserve the piano room"
        status = 0 # 0 is the non-post case
        context = {
            'timeline':timeline,
            'message':message,
            'status':status,
        }

        return render(request,'pianoroom_admin/index.html',context)
