from django.contrib import admin
from django.urls import path
from django.views.decorators.cache import cache_page
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from apps.views import UsersListCreateAPIView
from root import settings
from root.settings import CACHE_TTL, CACHE_KEY

urlpatterns = [
    path('users/', cache_page(CACHE_TTL, key_prefix=CACHE_KEY)(UsersListCreateAPIView.as_view()))
]
if settings.DEBUG:
    schema_view = get_schema_view(
        openapi.Info(
            title="Test Task API",
            default_version='v1',
            terms_of_service="https://www.google.com/policies/terms/",
            contact=openapi.Contact('GitHub', 'https://github.com/GaniyevUz/'),
            license=openapi.License(name='MIT License'),
        ),
        public=True,
        permission_classes=[permissions.AllowAny],
    )
    urlpatterns += [
        path('admin/', admin.site.urls),
        path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    ]
