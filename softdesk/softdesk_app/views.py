from rest_framework import viewsets, permissions
from django_filters import rest_framework as filters
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination

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

class CustomPagination(PageNumberPagination):
    page_size = 10  # Nombre d'éléments par page
    page_size_query_param = 'page_size'  # Paramètre pour spécifier la taille de la page
    max_page_size = 100  # Taille maximale de la page

# Dans votre ViewSet
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated, IsProjectContributor]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = ProjectFilter
    pagination_class = CustomPagination  # Utilisation de votre classe de pagination personnalisée

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
    permission_classes = [permissions.IsAuthenticated, IssuePermissions]
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    filterset_class = IssueFilter
    pagination_class = CustomPagination

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Issue, pk=pk)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, CommentPermissions]
    pagination_class = CustomPagination
class MySecureView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        message = f"Hello, {user.username}! You're authenticated."
        return Response({'message': message})
