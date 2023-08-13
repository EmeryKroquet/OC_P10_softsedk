from rest_framework import permissions

from .models import Issue


class IsProjectContributor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.project.contributors.filter(id=request.user.id).exists()

class ContributorPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        return view.action == 'list' and request.method in permissions.SAFE_METHODS


class IssuePermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        issue = view.get_object()  # Directly retrieve the issue from the view's queryset
        project = issue.project

        return project.contributors.filter(id=request.user.id).exists() or project.author == request.user
    """def has_permission(self, request, view):
        issue_id = view.kwargs.get('issue_id')
        issue = Issue.objects.get(id=issue_id)
        project = issue.project

        return project.contributors.filter(id=request.user.id).exists() or project.author == request.user"""""


class CommentPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        # Allow all GET requests (read permissions) for the comment list view
        return view.action == 'list' and request.method in permissions.SAFE_METHODS