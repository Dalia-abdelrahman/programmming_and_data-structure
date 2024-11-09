class Square:
    """Blueprint for square shape with input checks"""
    def __init__(self, measure=0):
        """Start a new square with validation checks
        
        Args:
            measure (int, optional): square dimension. Defaults to 0.
        """
        try:
            if not isinstance(measure, int):
                raise TypeError("size must be an integer")
            if measure < 0:
                raise ValueError("size must be >= 0")
        except Exception as error:
            raise error
            
        self.__measure = measure