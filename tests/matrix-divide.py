#!/usr/bin/python3
def matrix_divided(number_grid=None, factor=None):
    """
    Process matrix division operation.
    Args:
        number_grid: input number matrix
        factor: division factor
    Returns:
        Processed matrix with divided values
    """
    class MatrixValidator:
        @staticmethod
        def validate_matrix(grid):
            """Validates matrix structure and content"""
            if not isinstance(grid, list) or not grid:
                raise TypeError(MatrixValidator.ERROR_MATRIX)
            
            if not all(isinstance(row, list) for row in grid):
                raise TypeError(MatrixValidator.ERROR_MATRIX)
                
            reference_len = len(grid[0])
            if not all(len(row) == reference_len for row in grid):
                raise TypeError(MatrixValidator.ERROR_SIZE)
                
            if not all(isinstance(num, (int, float)) 
                      for row in grid for num in row):
                raise TypeError(MatrixValidator.ERROR_MATRIX)
                
        @staticmethod
        def validate_factor(value):
            """Validates division factor"""
            if not isinstance(value, (int, float)):
                raise TypeError(MatrixValidator.ERROR_DIV)
            if value == 0:
                raise ZeroDivisionError(MatrixValidator.ERROR_ZERO)
                
    # Error messages
    MatrixValidator.ERROR_MATRIX = "matrix must be a matrix (list of lists) of integers/floats"
    MatrixValidator.ERROR_SIZE = "Each row of the matrix must have the same size"
    MatrixValidator.ERROR_DIV = "div must be a number"
    MatrixValidator.ERROR_ZERO = "division by zero"

    # Validation
    MatrixValidator.validate_matrix(number_grid)
    MatrixValidator.validate_factor(factor)

    # Process division
    processed_grid = []
    for row in number_grid:
        processed_row = [round(element / factor, 2) for element in row]
        processed_grid.append(processed_row)
    
    return processed_grid
