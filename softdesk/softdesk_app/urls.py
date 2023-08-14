from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import CustomUserViewSet, ProjectViewSet, IssueViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'issues', IssueViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]

urlpatterns += router.urls
