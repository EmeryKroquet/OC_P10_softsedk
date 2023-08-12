from rest_framework import permissions


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
        # Allow all GET requests (read permissions) for the issue list view
        return view.action == 'list' and request.method in permissions.SAFE_METHODS

class CommentPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        # Allow all GET requests (read permissions) for the comment list view
        return view.action == 'list' and request.method in permissions.SAFE_METHODS