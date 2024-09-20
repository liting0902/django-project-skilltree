from django.urls import path
from . import views
from rest_framework import routers
# router = routers.DefaultRouter()
# router.register('api/project/<slug:project_slug>', views.all_data)

urlpatterns = [    
    path('', views.index, name='index'),
    path('skill-tree', views.skillTree),
    # path('api/project/<slug:project_slug>', views.all_data)
    
]