from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import UserModelViewSet
from todo.views import TodoViewset, TodoStatusViewset, ProjectViewset

router = DefaultRouter()
router.register('users', UserModelViewSet)
router.register('todo', TodoViewset)
router.register('status', TodoStatusViewset)
router.register('project', ProjectViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]
