from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import ValidationError
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from homework62.forms import IssueForm
from homework62.models import Issue, Project


class IssueDetail(DetailView):
    template_name = 'issue.html'
    model = Issue


class IssueUpdateView(UserPassesTestMixin, UpdateView):
    template_name = 'issue_update.html'
    form_class = IssueForm
    model = Issue

    def get_success_url(self):
        return reverse('issue_detail', kwargs={'pk': self.object.pk})

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)

    def test_func(self):
        return self.request.user in self.get_object().project.members.all() and self.request.user.has_perm(
            'homework62.change_issue')


class IssueDeleteView(UserPassesTestMixin, DeleteView):
    template_name = 'issue_delete.html'
    model = Issue
    context_object_name = 'issue'
    success_url = reverse_lazy('index')

    def test_func(self):
        return self.request.user in self.get_object().project.members.all() and self.request.user.has_perm(
            'homework62.delete_issue')
