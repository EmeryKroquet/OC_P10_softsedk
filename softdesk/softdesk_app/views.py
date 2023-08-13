from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions
from rest_framework.generics import get_object_or_404

from django_filters import rest_framework as filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CustomUser, Project, Issue, Comment
from .serializers import CustomUserSerializer, ProjectSerializer, IssueSerializer, CommentSerializer
from .permissions import IsProjectContributor, IssuePermissions


# Views for users
class UserListView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]

# Views for projects
class ProjectFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    author_id = filters.NumberFilter(field_name='author__id')
    type = filters.CharFilter(lookup_expr='exact')

    class Meta:
        model = Project
        fields = ['name', 'author_id', 'type']

class ProjectListView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProjectFilter

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]


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

class IssueListView(generics.ListCreateAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_class = IssueFilter

class IssueDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Issue, pk=pk)

# Views for comments
class CommentListView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]



class MySecureView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user  # The authenticated user
        message = f"Hello, {user.username}! You're authenticated."
        return Response({'message': message})