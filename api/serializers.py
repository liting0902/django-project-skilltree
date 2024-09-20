from rest_framework import serializers
from .models import Label,Project,SkillSet

class SkillItemSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.CharField(source='topic.id')
    topic = serializers.CharField(source='topic.name')
    rootid = serializers.CharField(source='rootid.id')
    parentid = serializers.CharField(source='parentid.id')
    class Meta:
        model= SkillSet
        fields = ['id','topic','expanded','rootid','parentid','direction','background_color','isroot']
class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Project
        fields = ('__all__')
class LabelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Label
        fields = ('__all__')