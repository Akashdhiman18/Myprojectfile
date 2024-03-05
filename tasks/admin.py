from django.contrib import admin

# Register your models here.
from tasks.models import Task # Register your models here. imports the Task model class from the models.py file of the tasks app (Tasks folder)
admin.site.register(Task) #registers this model class to be visible on the Django admin interface
