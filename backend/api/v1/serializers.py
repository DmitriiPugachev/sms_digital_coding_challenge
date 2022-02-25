"""API serializers."""


from rest_framework import serializers, validators

from items.models import Item


class ItemSerializer(serializers.ModelSerializer):
    """Item model serializer."""
    class Meta:
        model = Item
        fields = ("city", "start_date", "end_date", "price", "status", "color",)
