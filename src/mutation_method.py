import random
def mutation_flip_bit(solution):
    point = random.randint(0, len(solution) - 1)
    solution[point] = 1 - solution[point]
    return solution

def mutation_swap_bits(solution):
    point1 = random.randint(0, len(solution) - 1)
    point2 = random.randint(0, len(solution) - 1)
    solution[point1], solution[point2] = solution[point2], solution[point1]
    return solution
