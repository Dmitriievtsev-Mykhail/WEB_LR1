from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, LoginView, UserProfileView, AboutAppView, TaskViewSet

# Router автоматично генерує маршрути для ModelViewSet (GET, POST, PUT, DELETE)
router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/profile/', UserProfileView.as_view(), name='profile'),
    path('about/', AboutAppView.as_view(), name='about'),
    path('', include(router.urls)),
]