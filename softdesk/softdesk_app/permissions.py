from rest_framework import permissions

class IsProjectContributor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        project = obj.project if hasattr(obj, 'project') else None  # Get the project associated with the issue
        return project and project.contributors.filter(id=request.user.id).exists()


class IssuePermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        project = obj.project  # Get the project associated with the issue
        return project and (project.contributors.filter(id=request.user.id).exists() or project.author == request.user)


class CommentPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action == 'list':
            return True
        elif view.action in ['create', 'update', 'partial_update', 'destroy']:

            return True  # Si l'utilisateur a la permission
        else:
            return False  # Pour toute autre action, l'accès est refusé
