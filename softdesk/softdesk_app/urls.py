from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet, ProjectViewSet, IssueViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'issues', IssueViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    # Vos autres URLS
]

urlpatterns += router.urls
