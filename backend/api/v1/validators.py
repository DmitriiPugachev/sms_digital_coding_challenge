"""API v.1 validators."""


from rest_framework import validators


def end_date_validate(start_date, end_date, data):
    """Validate an end_date is after a start date."""
    if end_date < start_date:
        raise validators.ValidationError(
            {"end_date": "An end date must be after a start date."}
        )
    return data


def positive_number_validate(value):
    """Validate value is a positive number."""
    if value < 0.0:
        raise validators.ValidationError("A number must be positive.")
    return value
