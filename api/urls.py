from django.urls import path
from . import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register('skillsList', views.SkillView, basename='skillsList')
router.register('project', views.ProjectView, basename='project')
router.register('label', views.LabelView, basename='label')
urlpatterns = router.urls
# urlpatterns =[    
#     path('project', views.ProjectSkill.as_view())
# ]