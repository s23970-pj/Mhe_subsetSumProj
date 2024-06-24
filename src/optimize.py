import random


def subset_sum_objective(subset, target):
    return abs(sum(subset)==target)

def generate_neighbors_old(curent_solution, elements): # wszystkie możliwe kombinacje trzeba to zoptymalizować
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

def generate_random_solution_old(elements):
    return random.sample(elements, random.randint(1, len(elements)))

def generate_neighbors(current_solution):
    neighbors = []
    for i in range(len(current_solution)):
        # Flip one bit
        neighbor = current_solution[:]
        neighbor[i] = 1 - neighbor[i]
        neighbors.append(neighbor)

        # Optionally, flip two bits for additional neighbors
        for j in range(i + 1, len(current_solution)):
            neighbor2 = neighbor[:]
            neighbor2[j] = 1 - neighbor2[j]
            neighbors.append(neighbor2)

    return neighbors

def generate_random_solution(list_length):
    return [random.randint(0, 1) for _ in range(list_length)]

