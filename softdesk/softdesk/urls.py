from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('softdesk_app.urls')),  # Your app-specific URLs come first
    path('api/', include(router.urls)),  # Generic router URLs come last
]
