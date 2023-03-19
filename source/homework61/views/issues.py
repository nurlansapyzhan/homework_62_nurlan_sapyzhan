from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from homework61.forms import IssueForm
from homework61.models import Issue


class IssueDetail(DetailView):
    template_name = 'issue.html'
    model = Issue


class IssueUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'issue_update.html'
    form_class = IssueForm
    model = Issue

    def get_success_url(self):
        return reverse('issue_detail', kwargs={'pk': self.object.pk})

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)


class IssueCreateView(LoginRequiredMixin, CreateView):
    template_name = 'issue_create.html'
    model = Issue
    form_class = IssueForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = 1
        return context

    def get_success_url(self):
        return reverse('issue_detail', kwargs={'pk': self.object.pk})


class IssueDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'issue_delete.html'
    model = Issue
    context_object_name = 'issue'
    success_url = reverse_lazy('index')
