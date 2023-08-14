from rest_framework import permissions

class IsProjectContributor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        project = obj.project if hasattr(obj, 'project') else None  # Get the project associated with the issue
        return project and project.contributors.filter(id=request.user.id).exists()


class IssuePermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action == 'list':
            return True

        issue = view.get_object() if view.action in ['retrieve', 'update', 'partial_update', 'destroy'] else None
        project = issue.project if issue else None

        return project and (project.contributors.filter(id=request.user.id).exists() or project.author == request.user)


class CommentPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action == 'list':
            return True
