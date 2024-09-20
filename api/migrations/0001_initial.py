# Generated by Django 5.1 on 2024-09-18 15:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100)),
                ('isroot', models.BooleanField(default=True)),
                ('project_slug', models.SlugField(blank=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='SkillSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expanded', models.BooleanField(default=True)),
                ('direction', models.CharField(blank=True, max_length=100, null=True)),
                ('background_color', models.CharField(blank=True, max_length=100, null=True)),
                ('parentid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='api.label')),
                ('rootid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='project_skill', to='api.project')),
                ('topic', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='topics', to='api.label')),
            ],
        ),
    ]
