from django.contrib import admin
from .models import CustomUser, Project, Issue, Comment


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name',
                    'age', 'can_be_contacted', 'can_data_be_shared')
    list_filter = ('can_be_contacted', 'can_data_be_shared')
    search_fields = ('username', 'email', 'first_name', 'last_name')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'type')
    list_filter = ('type',)
    search_fields = ('name', 'author__username')


@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'priority',
                    'assigned_to', 'tag', 'project')
    list_filter = ('status', 'priority', 'tag', 'project')
    search_fields = ('title', 'description')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'author', 'issue')
    search_fields = ('text', 'author__username', 'issue__title')
