"""API serializers."""


from rest_framework import serializers
from django.core import validators

from api.v1.validators import end_date_validate, positive_number_validate
from items.models import Item


class ItemSerializer(serializers.ModelSerializer):
    """Item model serializer."""
    price = serializers.FloatField(validators=[positive_number_validate])
    EXPECTED_DATE_FORMAT = "%Y-%m-%d"

    class Meta:
        model = Item
        fields = (
            "city",
            "start_date",
            "end_date",
            "price",
            "status",
            "color",
        )

    def validate(self, data):
        """Validate an end date is after a start date."""
        return end_date_validate(
            start_date=data["start_date"],
            end_date=data["end_date"],
        )
