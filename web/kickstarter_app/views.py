from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Project


def project_list_view(request):
    projects = get_list_or_404(Project)
    context = {
        'projects': projects
    }

    return render(request, 'project/project.html', context)


def project_detail_view(request, pk=None):
    project = get_object_or_404(Project, pk)
    context = {
        'project': project
    }

    return render(request, 'projects/project_detail.html', context)
