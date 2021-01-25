from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Result, Parameter, Data

#here we set up the receiver functions
# check also the initalisation in the apps.py

@receiver(post_save, sender=Parameter)
def params_saved(sender,**kwargs):
    print("Parameters have been saved!")
    
@receiver(post_save, sender=Data)
def data_saved(sender,**kwargs):
    print("Data have been saved!")
