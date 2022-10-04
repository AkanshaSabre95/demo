
from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        exclude = ('id', 'title', 'description',  'assigned_to', 'start_date', 'end_date')