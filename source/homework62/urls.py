from django.urls import path

from homework62.views.base import IndexView, IndexRedirectView

from homework62.views.issues import IssueDetail, IssueUpdateView, IssueDeleteView

from homework62.views.projects import ProjectsView, ProjectDetail, ProjectCreate, IssueProjectCreate, \
    add_project_member, delete_project_member, ProjectDeleteView, ProjectUpdateView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('issue/', IndexRedirectView.as_view(), name='issue_index_redirect'),
    path('issue/<int:pk>', IssueDetail.as_view(), name='issue_detail'),
    path('issue/<int:pk>/update', IssueUpdateView.as_view(), name='issue_update'),
    path('issue/<int:pk>/delete', IssueDeleteView.as_view(), name='issue_delete'),
    path('projects', ProjectsView.as_view(), name='projects'),
    path('project/<int:pk>', ProjectDetail.as_view(), name='project_detail'),
    path('project/create', ProjectCreate.as_view(), name='project_create'),
    path('project/<int:pk>/delete', ProjectDeleteView.as_view(), name='project_delete'),
    path('project/<int:pk>/edit', ProjectUpdateView.as_view(), name='project_edit'),
    path('project/<int:pk>/create_issue', IssueProjectCreate.as_view(), name='issue_project_create'),
    path('project/<int:pk>/add_member', add_project_member, name='add_member'),
    path('project/<int:pk>/delete_member', delete_project_member, name='delete_member')
]
