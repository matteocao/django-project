from django.urls import path

# import the function to get the view
from . import views

# at URL '' I display what the function view.index tells me when I receive a get request <--> "path('', views.index, name='index')"
app_name = 'backend' # namespace
urlpatterns = [
    path('<int:pm_id>', views.compute, name='compute'),
    # ex: /polls/5/
]
