"""API v.1 URLs."""


from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.v1.views import ItemViewSet

router_v1 = DefaultRouter(trailing_slash="optional")
router_v1.register("items", ItemViewSet, basename="items")

urlpatterns = [
    path("", include(router_v1.urls)),
]
