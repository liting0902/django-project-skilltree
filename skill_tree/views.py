from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.urls import reverse
from django.template.loader import render_to_string
from api.models import  Project
from django.db.models import Avg, Count, Min, Sum
from django.core.serializers import serialize
from rest_framework import viewsets
# Create your views here.

def index(request):
    print("index")
    try:
        projects = Project.objects.all()
        for project in projects :
            print(project)
        return render(request,"app/index.html", {"projects":projects}) 
   
    except Exception as e:
        print(f"error : {e}")
        raise Http404()


   
def skillTree(request, ):
    try:        
        return render(request,"app/skill_tree.html")   

    except Exception as e:
        print(f"error : {e}")
        raise Http404()
