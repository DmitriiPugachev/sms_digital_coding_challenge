"""API v.1 validators."""


from rest_framework import validators


def end_date_validate(first_value, second_value):
    """Validate the first value is bigger than the second one."""
    if first_value < second_value:
        raise validators.ValidationError("End date must be bigger than start date.")
    return first_value
