from rest_framework import viewsets, permissions
from django_filters import rest_framework as filters
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from .models import CustomUser, Project, Issue, Comment
from .serializers import CustomUserSerializer, ProjectSerializer, IssueSerializer, CommentSerializer
from .permissions import IsProjectContributor, IssuePermissions, CommentPermissions

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated, IsProjectContributor]

class ProjectFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    author_id = filters.NumberFilter(field_name='author__id')
    type = filters.CharFilter(lookup_expr='exact')

    class Meta:
        model = Project
        fields = ['name', 'author_id', 'type']

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated, IsProjectContributor]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = ProjectFilter

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class IssueFilter(filters.FilterSet):
    class Meta:
        model = Issue
        fields = {
            'status': ['exact'],
            'priority': ['exact'],
            'assigned_to': ['exact'],
            'tag': ['exact'],
            'project': ['exact'],
        }

class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [permissions.IsAuthenticated, IssuePermissions]
    filterset_class = IssueFilter

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Issue, pk=pk)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, CommentPermissions]

class MySecureView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        message = f"Hello, {user.username}! You're authenticated."
        return Response({'message': message})
