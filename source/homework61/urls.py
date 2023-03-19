from django.urls import path

from homework61.views.base import IndexView, IndexRedirectView

from homework61.views.issues import IssueDetail, IssueUpdateView, IssueCreateView, IssueDeleteView

from homework61.views.projects import ProjectsView, ProjectDetail, ProjectCreate, IssueProjectCreate

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('issue/', IndexRedirectView.as_view(), name='issue_index_redirect'),
    path('issue/<int:pk>', IssueDetail.as_view(), name='issue_detail'),
    path('issue/<int:pk>/update', IssueUpdateView.as_view(), name='issue_update'),
    path('issue/create', IssueCreateView.as_view(), name='issue_create'),
    path('issue/<int:pk>/delete', IssueDeleteView.as_view(), name='issue_delete'),
    path('projects', ProjectsView.as_view(), name='projects'),
    path('project/<int:pk>', ProjectDetail.as_view(), name='project_detail'),
    path('project/create', ProjectCreate.as_view(), name='project_create'),
    path('project/<int:pk>/create_issue', IssueProjectCreate.as_view(), name='issue_project_create')
]
