
from django.urls import path
from . import views

from .views import MyTokenObtainPairView

from rest_framework_simplejwt.views import (
    TokenRefreshView,
    # TokenObtainPairView,
    # TokenVerifyView,
)


urlpatterns = [
    path('', views.apiOverview, name='api_overview'),
    path('task-list/', views.taskList, name='task-list'),
    path('task-details/<str:pk>/', views.taskDetails, name='task-details'),
    path('task-create/', views.taskCreate, name='task-create'),
    path('task-update/<str:pk>/', views.taskUpdate, name='task-update'),
    path('task-delete/<str:pk>/', views.taskDelete, name='task-delete'),

    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),



]
