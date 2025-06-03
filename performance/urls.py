from django.urls import path
from . import views


urlpatterns = [
    path('performance/',views.performanceListCreate.as_view(), name="performance-view-create")
]
