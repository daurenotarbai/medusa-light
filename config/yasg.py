from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import re_path, path

schema_view = get_schema_view(
    openapi.Info(
        title="Medusa Light API Documentation",
        default_version='v1',
        description="Simple news project!",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="daurenotarbai.00@gmail.com"),

    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('documentation/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger_ui'),
]
