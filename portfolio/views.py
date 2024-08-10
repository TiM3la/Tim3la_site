from django.shortcuts import render, get_object_or_404
from .models import Project, Links

def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects' : projects})

def project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'portfolio/img.html', {'project':project})

def links(request):
    links = Links.objects.all()
    return render(request, 'portfolio/links.html', {'links': links})
    pass