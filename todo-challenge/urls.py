
from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .apps.tasks.views import TaskListCreateView, TaskDetailView, LabelListCreateView, LabelDetailView


urlpatterns = [
    path('', lambda request: redirect('admin/')),
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('api/tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('api/labels/', LabelListCreateView.as_view(), name='label-list-create'),
    path('api/labels/<int:pk>/', LabelDetailView.as_view(), name='label-detail'),
]
