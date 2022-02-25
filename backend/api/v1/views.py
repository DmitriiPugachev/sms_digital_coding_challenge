"""API views."""


from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from api.v1.serializers import ItemSerializer
from api.v1.filters import ItemFilter
from items.models import Item


class ItemViewSet(viewsets.ModelViewSet):
    """Item model ViewSet."""
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = ItemFilter
