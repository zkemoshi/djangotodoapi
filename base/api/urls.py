
from django.urls import path
from . import views

# from .views import MyTokenObtainPairView

from .views import register, UserLoginView, task_list, task_detail


from rest_framework_simplejwt.views import (
    TokenRefreshView,
    # TokenObtainPairView,
    # TokenVerifyView,
)


urlpatterns = [
    path('register/', register),
    path('login/', UserLoginView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('tasks/', task_list),
    path('tasks/<int:pk>/', task_detail),
]
