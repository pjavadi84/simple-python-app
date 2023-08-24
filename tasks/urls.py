from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet
from django.contrib import admin


router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/', include('tasks.urls')),
]
