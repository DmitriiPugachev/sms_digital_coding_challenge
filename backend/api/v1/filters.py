"""API v.1 custom filters."""


from django_filters.filters import DateFromToRangeFilter
from django_filters.rest_framework import FilterSet

from items.models import Item


class ItemFilter(FilterSet):
    """Filter Item objects by start date and end date."""
    start_date = DateFromToRangeFilter(field_name="start_date")
    end_date = DateFromToRangeFilter(field_name="end_date")

    class Meta:
        model = Item
        fields = (
            "start_date",
            "end_date",
        )
