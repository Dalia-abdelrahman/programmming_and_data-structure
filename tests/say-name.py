#!/usr/bin/python3
def say_my_name(primary_name=None, secondary_name=""):
    """
    Output formatted name string.
    Args:
        primary_name: main name component
        secondary_name: additional name component
    """
    class NameProcessor:
        def __init__(self, primary, secondary):
            self.primary = primary
            self.secondary = secondary
            self.validate_inputs()

        def validate_inputs(self):
            """Validate all name inputs"""
            if not isinstance(self.primary, str):
                raise TypeError("first_name must be a string")
            if not isinstance(self.secondary, str):
                raise TypeError("last_name must be a string")

        def format_output(self):
            """Create formatted name string"""
            return f"My name is {self.primary} {self.secondary}"

        def display(self):
            """Display the formatted name"""
            print(self.format_output())

    # Process and display name
    processor = NameProcessor(primary_name, secondary_name)
    processor.display()
