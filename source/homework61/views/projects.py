from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from homework61.models import Project, Issue

from homework61.forms import ProjectForm, IssueForm, IssueProjectForm


class ProjectsView(ListView):
    template_name = 'projects.html'
    model = Project
    context_object_name = 'projects'


class ProjectDetail(DetailView):
    template_name = 'project_detail.html'
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.get_object()
        context['issues'] = Issue.objects.all().exclude(is_deleted=True).filter(project=project.pk)
        return context


class ProjectCreate(LoginRequiredMixin, CreateView):
    template_name = 'project_create.html'
    model = Project
    form_class = ProjectForm

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk})


class IssueProjectCreate(LoginRequiredMixin, CreateView):
    template_name = 'issue_project_create.html'
    model = Project
    form_class = IssueProjectForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.get_object()
        context['project'] = project
        return context

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        form.instance.project = project
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('issue_detail', kwargs={'pk': self.object.pk})
