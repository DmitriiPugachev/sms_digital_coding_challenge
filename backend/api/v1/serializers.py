"""API serializers."""


from datetime import datetime

from rest_framework import serializers

from items.models import Item
from api.v1.validators import end_date_validate


class ItemSerializer(serializers.ModelSerializer):
    """Item model serializer."""
    EXPECTED_DATE_FORMAT = "%Y-%m-%d"

    class Meta:
        model = Item
        fields = ("city", "start_date", "end_date", "price", "status", "color",)

    def validate_end_date(self, value):
        """Validate an end date is bigger than a start date."""
        start_date = self.context["request"].data["start_date"]
        start_date_formatted = datetime.strptime(start_date, self.EXPECTED_DATE_FORMAT).date()
        return end_date_validate(
            first_value=value, second_value=start_date_formatted
        )
