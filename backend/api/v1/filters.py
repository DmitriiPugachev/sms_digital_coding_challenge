"""API v.1 custom filters."""

from django_filters.filters import DateFromToRangeFilter
from django_filters.rest_framework import FilterSet

from items.models import Item


class ItemFilter(FilterSet):
    """Item custom filter for start_date and end_date date pickers."""
    start_date = DateFromToRangeFilter(field_name="start_date")
    end_date = DateFromToRangeFilter(field_name="end_date")

    class Meta:
        model = Item
        fields = ("start_date", "end_date",)
