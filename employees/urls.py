from django.urls import path
from . import views

urlpatterns = [
    path("employees/", views.employeeListCreate.as_view(), name="employee-view-create")
]
