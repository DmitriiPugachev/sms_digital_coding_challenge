"""A management commands for fulfilling a database."""


import json

from datetime import datetime
from django.core.management.base import BaseCommand

from items.models import Item


class Command(BaseCommand):
    """Command definition."""
    help = "Load items data from JSON file to DB"

    def handle(self, *args, **options):
        """A method for fulfilling database with items data from JSON file."""
        with open("items/data/data.json", encoding="utf-8") as file:
            load = json.load(file)
            for item in load:
                city = item.get("city", None)
                start_date = datetime.strptime(item.get("start_date", None), "%m/%d/%Y")
                end_date = datetime.strptime(item.get("end_date", None), "%m/%d/%Y")
                price = float(item.get("price", None))
                status = item.get("status", None)
                color = item.get("color", None)
                Item.objects.get_or_create(
                    city=city,
                    start_date=start_date,
                    end_date=end_date,
                    price=price,
                    status=status,
                    color=color,
                )
