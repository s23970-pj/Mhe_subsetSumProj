def generate_neighbors(curent_solution, elements): # wszystkie możliwe liczy zoptymalizować
    neighbors = []
    for element in elements:
        if element not in curent_solution: #jezeli element nie znajduje się
            new_solution = curent_solution + [element]
            neighbors.append(new_solution)
        else:
            new_solution=curent_solution.copy()
            new_solution.remove(element)
            neighbors.append(new_solution)
    return neighbors