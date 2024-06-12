import random


def subset_sum_objective(subset, target):
    return sum(subset)==target

def generate_neighbor(curent_solution, elements):
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

def generate_random_solution(elements):
    return random.sample(elements, random.randint(1, len(elements)))

