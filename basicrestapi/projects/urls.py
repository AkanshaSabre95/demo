from django.urls import path, include

from rest_framework import routers
from .views import ProjectViewSet
from .import views

routers = routers.DefaultRouter()
routers.register(r'projects', views.ProjectViewSet)

urlpatterns = [
    path('',include(routers.urls)),
    path('api-auth/', include('rest_framework.urls',namespace='rest_framework')),
]