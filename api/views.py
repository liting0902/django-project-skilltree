from django.http import HttpResponse, JsonResponse
from rest_framework import generics, viewsets, response
from rest_framework.decorators import api_view
from .serializers import SkillItemSerializer, ProjectSerializer, LabelSerializer
from .models import Label,SkillSet, Project
from django.core.serializers import serialize
# Create your views here.
# @api_view(['GET'])
# def SkillView(request):
#     queryset = SkillSet.objects.all()
#     res = SkillItemSerializer(queryset, many=True)
#     return response.Response(res.data)

class SkillView(viewsets.ModelViewSet):
    serializer_class = SkillItemSerializer

    def get_queryset(self):
        project_name = self.request.query_params.get('category')
        print()
        queryset = Project.objects.get(project_slug = project_name).project_skill.all()
        return queryset
    
class ProjectView(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    def get_queryset(self):
        queryset = Project.objects.all()
        return queryset
    
class LabelView(viewsets.ModelViewSet):
    serializer_class = LabelSerializer
    def get_queryset(self):
        queryset = Label.objects.all()
        return queryset