from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from homework62.models import Project, Issue

from homework62.forms import ProjectForm, IssueForm, IssueProjectForm


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
        context['members'] = project.members.all()
        return context


class ProjectCreate(LoginRequiredMixin, CreateView):
    template_name = 'project_create.html'
    model = Project
    form_class = ProjectForm

    def form_valid(self, form):
        project = form.save(commit=False)
        project.save()
        project.members.add(self.request.user)
        return super().form_valid(form)

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


def add_project_member(request, pk):
    project = get_object_or_404(Project, pk=pk)
    users = User.objects.all()
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        user = get_object_or_404(User, pk=user_id)
        project.members.add(user)
        return redirect('project_detail', pk=pk)
    return render(request, 'add_project_member.html', context={'project': project, 'users': users})


def delete_project_member(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        user = get_object_or_404(User, pk=user_id)
        project.members.remove(user)
        return redirect('project_detail', pk=pk)
    return render(request, 'delete_project_member.html', context={'project': project})
