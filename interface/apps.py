from django.apps import AppConfig
from django.db.models.signals import post_save


class InterfaceConfig(AppConfig):
    name = 'interface'
    # this function is to connect signals senders and receivers
    def ready(self):
            # importing model classes
            from .models import Result, Parameter, Data  # or...
            from .signals import data_saved, params_saved
            Parameter = self.get_model('Parameter')
            Data = self.get_model('Data')
            # registering signals with the model's string label
            post_save.connect(params_saved, sender='interface.Parameter')
            post_save.connect(data_saved, sender='interface.Data')
