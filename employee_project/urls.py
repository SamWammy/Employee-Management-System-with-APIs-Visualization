from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.shortcuts import redirect

def redirect_to_docs(request):
    return redirect('schema-swagger-ui')

# Swagger schema view config
schema_view = get_schema_view(
   openapi.Info(
      title="Employee Project API",
      default_version='v1',
      description="API documentation for Employee Management System",
      contact=openapi.Contact(email="your@email.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",redirect_to_docs),
    path("employees/", include("employees.urls")),
    path("attendence/", include("attendence.urls")),
    path("performance/", include("performance.urls")),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path("swagger/", schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path("redoc/", schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
