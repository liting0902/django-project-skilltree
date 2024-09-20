from django.contrib import admin
from .models import  Label,SkillSet,Project
# Register your models here.
class label_admin(admin.ModelAdmin):
    list_display=("id","name")

admin.site.register(Label, label_admin)

class skill_admin(admin.ModelAdmin):
    list_display=("topic__name","background_color","expanded","parentid","direction","rootid__project_name")
admin.site.register(SkillSet, skill_admin)

class project_admin(admin.ModelAdmin):
    list_display=("id","project_name","isroot")
admin.site.register(Project,project_admin)

