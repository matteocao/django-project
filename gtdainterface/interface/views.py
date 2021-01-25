from django.shortcuts import render
from django.urls import reverse
from django.http import request, HttpResponse, Http404, HttpResponseRedirect, StreamingHttpResponse
from django.core.files.storage import FileSystemStorage
from .models import Data, Result, Parameter
from django.conf import settings
from django.utils.safestring import mark_safe
import requests
import time
import django_rq
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def params_view(request, data):
    context = {'user_id': request.user, 'data_id' : data}
    return render(request, 'interface/params.html',context)
    #return HttpResponse("hello world")

@login_required
def update_params(request, data_id):
# here save in database
    data = Data.objects.get(pk=data_id)
    print(request.POST['homology'])
    print(request.POST['maxEdgeLength'])
    pm = Parameter.objects.create(data=data,
                             max_edge_length=request.POST['maxEdgeLength'],
                             homology=request.POST['homology'])
    ## send a request to /backend for computation to the computing server
    #print("sending signal from update_params")
    URL = 'http://'+request.META['HTTP_HOST'] + reverse('backend:compute',args=(pm.id,))
    r = requests.get(url=URL)
    #print("output")
    #print(r.text)
    #reverse('backend:compute',args=(pm.id,)
    return HttpResponseRedirect(reverse('interface:results',args=(r.text,)))

@login_required
def upload_data_view(request):
    context = {'user_id': request.user}
    return render(request, 'interface/upload.html',context)

@login_required
def upload_data(request):
# here save in database
    file_name = request.POST['fname']
    file = request.FILES['file']
    print(file.name) # form attribute enctype="multipart/form-data"
    print(file.size)
    fs = FileSystemStorage() # saving to MEDIA_ROOT
    real_name = fs.save(file_name,file)
    dt = Data.objects.create(dataset_url=settings.MEDIA_URL + real_name,dataset_name=file_name)
    context = {'user_id': request.user}
    return HttpResponseRedirect(reverse('interface:params', args=(dt.id,)))
    
@login_required
def results_view(request, job_id):
# here display the results of the analysis
    #time.sleep(3)
    context = {'user_id': request.user, 'job_id': job_id}
    return render(request,'interface/results.html',context)

@login_required
def get_results(request, job_id):
    queue = django_rq.get_queue('default')
    job2 = queue.fetch_job(job_id)
    #print('results : ', job2.result)
    while job2.result is None:
        time.sleep(1)
    #print('results : ', job2.result)
    res_id=job2.result
    plot = mark_safe(Result.objects.get(pk=res_id).result)
    return HttpResponse(plot)

