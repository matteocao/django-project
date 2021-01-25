from django.contrib import admin

# Register your models here.
from .models import Data, Parameter, Result

class ParameterAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Max Length', {'fields': ['max_edge_length']}),
        ('Homology', {'fields': ['homology']}),
    ]

    list_display = ('max_edge_length', 'homology')
    list_filter = ['max_edge_length']
    search_fields = ['homology']
    
    
admin.site.register(Parameter, ParameterAdmin)
admin.site.register(Data)
admin.site.register(Result)
