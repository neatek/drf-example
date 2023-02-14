import os
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include, re_path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from .views import UserModelViewSet
from todo.views import TodoViewset, ProjectViewset
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import TokenVerifyView
from rest_framework import permissions
from graphene_django.views import GraphQLView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = DefaultRouter()
router.register("users", UserModelViewSet)
router.register("todo", TodoViewset)
router.register("project", ProjectViewset)

schema_view = get_schema_view(
    openapi.Info(
        title="Library",
        default_version="0.1",
        description="Documentation to out project",
        contact=openapi.Contact(email="admin@admin.local"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    # Admin panel
    path("admin/", admin.site.urls),
    # API
    path("api/", include(router.urls)),
    # Auth
    path("api-token-auth/", views.obtain_auth_token),
    path("api-auth/", include("rest_framework.urls")),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    # GraphQL
    path("graphql/", GraphQLView.as_view(graphiql=True)),
    # Documents
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    re_path(
        r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),
]

# React frontend can be served by nginx
# Static files can be served by nginx
# urlpatterns += static(settings.FRONTEND_URL, document_root=settings.FRONTEND_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
