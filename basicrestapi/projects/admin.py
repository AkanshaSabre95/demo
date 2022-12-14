from django.contrib import admin

from .models import Project

# Register your models here.


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    fields= ('title', 'description',  'assigned_to', 'start_date', 'end_date')