"""gtdainterface URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

app_name = 'interface'
urlpatterns = [
    path('', views.upload_data_view, name='upload_data_view'),
    path('upload_data', views.upload_data, name='upload_data'),
    path('params/<int:data>/', views.params_view, name='params'),
    path('update_params/<int:data_id>/', views.update_params, name='update_params'),
    path('results/<job_id>/', views.results_view, name='results'),
    path('get_results/<job_id>/', views.get_results, name='get_results'),
]
