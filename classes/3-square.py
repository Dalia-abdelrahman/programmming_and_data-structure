class Square:
    """Blueprint for square shape with area computation"""
    
    def __init__(self, width=0):
        """Initialize square object
        
        Args:
            width (int, optional): width of square. Defaults to 0.
            
        Attributes:
            __width (int): private storage of square width
        """
        try:
            self.validate_and_set_width(width)
        except Exception as error:
            raise error
    
    def validate_and_set_width(self, value):
        """Check and set width value
        
        Args:
            value: width to validate and set
        """
        if not str(value).isdigit() and value != 0:
            raise TypeError("size must be an integer")
        if int(value) < 0:
            raise ValueError("size must be >= 0")
        self.__width = int(value)
    
    def area(self):
        """Find square area
        
        Returns:
            int: calculated area of square
        """
        return self.__width * self.__width