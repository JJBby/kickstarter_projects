from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.core.paginator import Paginator
from .models import Project


def project_list_view(request):
    projects = get_list_or_404(Project)
    # paginator = Paginator(projects, 50)
    #
    # page = request.GET.get('page')
    # something = paginator.get_page(page)

    context = {
        'projects': projects
    }

    return render(request, 'project/project_list.html', context=context)


def project_detail_view(request, pk=None):
    project = get_object_or_404(Project, pk)
    context = {
        'project': project
    }

    return render(request, 'project/project_detail.html', context=context)
