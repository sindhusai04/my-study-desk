from django.contrib import admin
from . models import *

#ADMIN PANEL
admin.site.register(Notes)        
admin.site.register(Homework)
admin.site.register(Todo)      