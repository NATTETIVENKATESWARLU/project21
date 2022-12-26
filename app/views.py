from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):
    forms=Topic_forms()
    d={'forms':forms}
    if request.method=='POST':
        form_data=Topic_forms(request.POST)
        if form_data.is_valid():
            form_data.save()
            return HttpResponse('yes insert data')
        
    return render(request,'insert_topic.html',d)



def insert_webpage(request):
    forms=web_forms()
    d={'forms':forms}
    if request.method=='POST':
        form_data=web_forms(request.POST)
        if form_data.is_valid():
            form_data.save()
            return HttpResponse('yes insert data')
        
    return render(request,'insert_webpage.html',d)




def insert_a_r(request):
    forms=A_R_forms()
    d={'forms':forms}
    if request.method=='POST':
        form_data=A_R_forms(request.POST)
        if form_data.is_valid():
            form_data.save()
            return HttpResponse('yes insert data')
        
    return render(request,'insert_a_r.html',d)