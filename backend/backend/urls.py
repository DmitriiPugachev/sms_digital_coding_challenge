"""Project URLs."""


from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
]

schema_view = get_schema_view(
    openapi.Info(
        title="Coding challenge API",
        default_version="v1",
        description="Coding challenge project api app documentation",
        contact=openapi.Contact(email="admin@admin.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
    url(
        r"^redoc/$",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
]
