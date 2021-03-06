"""Items admin config."""


from django.contrib import admin

from items.models import Item


class ItemAdmin(admin.ModelAdmin):
    """Item model admin config."""
    list_display = (
        "city",
        "start_date",
        "end_date",
        "price",
        "status",
        "color",
    )
    search_fields = ("city",)
    list_filter = (
        "start_date",
        "end_date",
        "status",
    )
    empty_value_display = "-empty-"


admin.site.register(Item, ItemAdmin)
