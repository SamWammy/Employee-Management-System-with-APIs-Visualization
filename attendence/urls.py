from . import views
from django.urls import path 

urlpatterns = [
    path("attendence/",views.attendenceListCreate.as_view(), name="attendence-view-create")
]
