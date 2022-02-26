"""API v.1 validators."""


from rest_framework import validators


def end_date_validate(start_date, end_date):
    """Validate an end_date is bigger than a start date."""
    if end_date < start_date:
        raise validators.ValidationError(
            "An end date must be bigger than a start date."
        )
    return end_date


def positive_float_validate(value, field_name):
    """Validate value is a positive float."""
    if not isinstance(value, float):
        raise validators.ValidationError(f"{field_name} must be a float.")
    if value < 0.0:
        raise validators.ValidationError(
            f"{field_name} must be a positive float."
        )
    return value
