"""Items models description."""


from colorfield.fields import ColorField
from django.core.validators import MinValueValidator
from django.db import models


class ItemStatuses:
    """Constant item statuses."""
    NEVER = "Never"
    ONCE = "Once"
    SELDOM = "Seldom"
    OFTEN = "Often"
    DAILY = "Daily"
    WEEKLY = "Weekly"
    MONTHLY = "Monthly"
    YEARLY = "Yearly"
    ITEM_STATUSES_CHOICES = [
        (NEVER, NEVER),
        (ONCE, ONCE),
        (SELDOM, SELDOM),
        (OFTEN, OFTEN),
        (DAILY, DAILY),
        (WEEKLY, WEEKLY),
        (MONTHLY, MONTHLY),
        (YEARLY, YEARLY),
    ]


class Item(models.Model):
    """Item model description."""
    city = models.CharField(
        max_length=200,
        verbose_name="Item city name",
    )
    start_date = models.DateField(
        db_index=True,
        verbose_name="Item start date",
    )
    end_date = models.DateField(
        db_index=True,
        verbose_name="Item end date",
    )
    price = models.FloatField(
        validators=[MinValueValidator(0.0)],
        verbose_name="Item price",
    )
    status = models.CharField(
        max_length=50,
        choices=ItemStatuses.ITEM_STATUSES_CHOICES,
        verbose_name="Item status",
    )
    color = ColorField(
        format="hex",
        verbose_name="Item color",
    )

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"

    def __str__(self):
        """Returns string view of a city field."""
        return self.city
