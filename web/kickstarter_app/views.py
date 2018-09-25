from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.core.paginator import Paginator
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.conf import settings
from .models import Project


CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)



def project_list_view(request):
    projects_query = get_list_or_404(Project)
    paginator = Paginator(projects_query, 30)

    page = request.GET.get('page')
    projects = paginator.get_page(page)

    context = {
        'projects': projects
    }

    return render(request, 'project/project_list.html', context=context)


def project_detail_view(request, pk=None):
    project = get_object_or_404(Project, id=pk)
    context = {
        'project': project
    }

    return render(request, 'project/project_detail.html', context=context)
