def pascal_triangle(n):
    if n <= 0:
        return []
    
    triangle = [[1]]
    
    for level_index in range(1, n):
        current_level = [1]

        for element_index in range(1, level_index):
            current_level.append(triangle[level_index-1][element_index-1] + triangle[level_index-1][element_index])

        current_level.append(1)
        triangle.append(current_level)
    
    return triangle
