from django.shortcuts import render
from django.urls import reverse
from django.http import request, HttpResponse, HttpResponseRedirect
import pandas as pd
import numpy as np
import plotly
import plotly.graph_objects as go
from interface.models import Result, Parameter
from interface.views import update_params
import django_rq
import requests
import time

user_id = 100

def computeAndPlot(nn, pm_id):
    param = Parameter.objects.get(pk=pm_id)
    X=np.random.random((nn,2))
    df = pd.DataFrame(X,columns=["x1","x2"])
    fig = go.Figure(data=go.Scatter(x=df['x1'].values, y=df['x2'].values, mode='markers'))
    svg = plotly.io.to_image(fig, format='svg')
    res = Result.objects.create(parameter=param,
                            result=svg.decode("utf-8"),
                            diagram=df.to_dict())
    return res.id

# Create your views here.
def compute(request, pm_id): # expects pm_id
    # launching a job on redis server
    job=django_rq.enqueue(computeAndPlot, args=(10, pm_id,))
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



