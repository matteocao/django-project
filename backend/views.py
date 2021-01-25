from django.shortcuts import render
from django.urls import reverse
from django.http import request, HttpResponse, HttpResponseRedirect
import pandas as pd
import numpy as np
import plotly
import plotly.graph_objects as go
from interface.models import Result, Parameter, Data
from interface.views import update_params
import django_rq
import requests
import time
import io
import dropbox
from django.conf import settings



def computeAndPlot(dbx, pm_id):
    param = Parameter.objects.get(pk=pm_id)
    #get remote file path
    data_file = param.data.dataset_file.name
    # extract metadata and content
    metadata, result = dbx.files_download(data_file)
    data_str = io.StringIO(result.content.decode('utf-8'))
    df = pd.read_csv(data_str,sep=",")
    #print(df)
    #X=np.random.random((nn,2))
    #df = pd.DataFrame(X,columns=["x1","x2"])
    fig = go.Figure(data=go.Scatter(x=df['x1'].values, y=df['x2'].values, mode='markers'))
    svg = plotly.io.to_image(fig, format='svg')
    res = Result.objects.create(parameter=param,
                            result=svg.decode("utf-8"),
                            diagram=df.to_dict())
    return res.id

# Create your views here.
def compute(request, pm_id): # expects pm_id
    dbx = dropbox.Dropbox(settings.DROPBOX_OAUTH2_TOKEN)
    # launching a job on redis server
    job = django_rq.enqueue(computeAndPlot, args=(dbx, pm_id,))
    #print('Job id: %s' % job.id)
    #print('Job id: %s' % job.get_status())
    #print("saving to db:")
    #time.sleep(3)
    #print('Job id: %s' % job.get_status())
    #print('results : ', job.result)
    #redis_conn = django_rq.get_connection('default')
    #queue = django_rq.get_queue('default')
    #print("queue: ", queue)
    #print("connection: ", redis_conn)
    #job2 = queue.fetch_job(job.id)
    #print('results : ', job2.result)
    #print("the result id is:")
    #print(res.id)
    return HttpResponse(job.id)



