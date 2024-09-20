from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify


class Project(models.Model):
    project_name=models.CharField(max_length=100)
    isroot=models.BooleanField(default=True)
    project_slug = models.SlugField(default="",blank=True, null=False, db_index=True)# db_index=True => For SEO
    def save(self,*args,**kwargs):
        self.project_slug = slugify(self.project_name)
        super().save(*args,**kwargs)
    def __str__(self):         
        return f"{self.id} , project_name:{self.project_name}"
       
class Label(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):         
        return f"{self.id}"    

class SkillSet(models.Model):
    topic=models.ForeignKey(Label, on_delete= models.PROTECT, null=True, related_name="topics")
    expanded=models.BooleanField(default=True)
    isroot=models.BooleanField(default=False)
    rootid = models.ForeignKey(Project, on_delete= models.PROTECT, null=True, related_name="project_skill")
    parentid=models.ForeignKey(Label, on_delete= models.PROTECT, null=True)
    direction=models.CharField(max_length=100,blank=True, null=True)
    background_color=models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):         
        return f"id:{self.id} , topic:{self.topic.name}, expanded:{self.expanded}, rootid:{self.rootid}, parentid:{self.parentid}, direction:{self.direction}, background_color:{self.background_color}"
    


