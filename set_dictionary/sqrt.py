def square_matrix_simple(matrix) :
    new_matrix = [ ]
    for row in matrix :
        new_row = [element ** 2 for element in row]
        new_matrix.append(new_row)
    return new_matrix
[09/11, 4:07 pm] Dalia: def search_replace(my_list, search, replace) :
    new_list = [replace if element == search else element for element in my_list]
    return new_list