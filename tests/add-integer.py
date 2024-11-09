#!/usr/bin/python3
def add_integer(val_x=None, val_y=98):
    """
    Computes sum of two values after integer conversion.
    Args:
        val_x: primary number (required)
        val_y: secondary number (optional, default=98)
    Returns:
        Sum as integer
    """
    def validate_numeric(value, name):
        """Validates if value is numeric type"""
        if not value:
            raise TypeError(f"{name} must be an integer")
        if not any([isinstance(value, numeric_type) 
                   for numeric_type in [int, float]]):
            raise TypeError(f"{name} must be an integer")
        return int(value)

    x = validate_numeric(val_x, 'a')
    y = validate_numeric(val_y, 'b')
    
    computed_sum = x + y
    return computed_sum
