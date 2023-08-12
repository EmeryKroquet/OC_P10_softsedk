from rest_framework import serializers
from .models import CustomUser, Project, Issue, Comment

# Serializer pour l'utilisateur (CustomUser)
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'age', 'can_be_contacted', 'can_data_be_shared']

# Serializer pour le projet (Project)
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'type', 'author']

# Serializer pour le problème (Issue)
class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ['id', 'title', 'description', 'status', 'priority', 'assigned_to', 'tag', 'project']

# Serializer pour le commentaire (Comment)
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'text', 'author', 'issue']