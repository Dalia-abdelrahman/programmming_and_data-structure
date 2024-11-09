#!/usr/bin/python3

def print_sequence_safely(sequence=None, num_elements=0):
    """
    Print elements from a sequence with safety checks
    
    Parameters:
        sequence (list): Sequence to print from (defaults to None)
        num_elements (int): Target number of elements to print
    
    Returns:
        int: Count of actually printed elements
    """
    if sequence is None:
        sequence = []
        
    print_counter = 0
    elements_printed = []
    
    try:
        while print_counter < num_elements:
            current_element = sequence[print_counter]
            elements_printed.append(str(current_element))
            print_counter += 1
            
    except (IndexError, TypeError):
        pass
    
    print("".join(elements_printed))
    return print_counter


def process_numeric_inputs(*input_values):
    """
    Process and sum numeric inputs, ignoring non-numeric values
    
    Parameters:
        *input_values: Variable number of inputs to process
    
    Returns:
        float: Sum of all valid numeric inputs
    """
    running_sum = 0.0
    
    for value in input_values:
        if process_single_value(value):
            running_sum += process_single_value(value)
            
    return running_sum


def process_single_value(value):
    """
    Helper function to process a single value
    
    Parameters:
        value: Value to process
    
    Returns:
        float or None: Processed numeric value or None if invalid
    """
    try:
        return float(value)
    except (ValueError, TypeError):
        return None


def execute_test_scenarios():
    """
    Execute comprehensive test scenarios for both functions
    """
    # Scenario 1: Standard numeric list
    print("\nScenario 1: Standard numeric list")
    test_numbers = [5, 10, 15, 20, 25]
    successful_prints = print_sequence_safely(test_numbers, 3)
    print(f"Successfully printed: {successful_prints} elements")

    # Scenario 2: Mixed content list
    print("\nScenario 2: Mixed content list")
    test_mixed = ["start", 42, 3.14, {"key": "value"}, [1, 2, 3]]
    successful_prints = print_sequence_safely(test_mixed, 4)
    print(f"Successfully printed: {successful_prints} elements")

    # Scenario 3: Edge case - empty list
    print("\nScenario 3: Edge case - empty list")
    successful_prints = print_sequence_safely([], 2)
    print(f"Successfully printed: {successful_prints} elements")

    # Scenario 4: Edge case - None input
    print("\nScenario 4: Edge case - None input")
    successful_prints = print_sequence_safely(None, 3)
    print(f"Successfully printed: {successful_prints} elements")

    # Scenario 5: Numeric processing - clean input
    print("\nScenario 5: Numeric processing - clean input")
    clean_sum = process_numeric_inputs(1, 2.5, "3.7", 4)
    print(f"Clean sum result: {clean_sum}")

    # Scenario 6: Numeric processing - mixed input
    print("\nScenario 6: Numeric processing - mixed input")
    mixed_sum = process_numeric_inputs(
        10,
        "invalid",
        "20.5",
        [30],
        {"value": 40},
        "50.7"
    )
    print(f"Mixed sum result: {mixed_sum}")


if __name__ == "__main__":
    execute_test_scenarios()