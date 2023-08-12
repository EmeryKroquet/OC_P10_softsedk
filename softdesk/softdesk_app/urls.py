# urls.py

from django.urls import path
from .views import (
    UserListView, UserDetailView,
    ProjectListView, ProjectDetailView,
    IssueListView, IssueDetailView,
    CommentListView, CommentDetailView
)

urlpatterns = [
    # URLs pour les utilisateurs
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),

    # URLs pour les projets
    path('projects/', ProjectListView.as_view(), name='project-list'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),

    # URLs pour les problèmes (issues)
    path('issues/', IssueListView.as_view(), name='issue-list'),
    path('issues/<int:pk>/', IssueDetailView.as_view(), name='issue-detail'),

    # URLs pour les commentaires
    path('comments/', CommentListView.as_view(), name='comment-list'),
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
]

