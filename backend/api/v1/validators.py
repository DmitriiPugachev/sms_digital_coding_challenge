"""API v.1 validators."""


from rest_framework import validators


def end_date_validate(first_value, second_value, first_value_name, second_value_name):
    """Validate the first value is bigger than the second one."""
    if first_value < second_value:
        raise validators.ValidationError(
            f"{first_value_name} must be bigger than {second_value_name}."
        )
    return first_value


def positive_float_validate(value, field_name):
    """Validate value is a positive float."""
    if not isinstance(value, float):
        raise validators.ValidationError(f"{field_name} must be a float.")
    if value < 0.0:
        raise validators.ValidationError(
            f"{field_name} must be a positive float."
        )
    return value
