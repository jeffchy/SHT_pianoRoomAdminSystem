from django.http import HttpResponse
from django.shortcuts import render
from .models import Reserve
from django.http import Http404

def index(request):
    context = {
        'textcode':'frog'
    }



    return render(request,'pianoroom_admin/index.html',context)
