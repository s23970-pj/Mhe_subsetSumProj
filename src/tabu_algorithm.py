from optimize import generate_random_solution

def tabu_search(elements, target, tabu_size, r):
    current_solution=generate_random_solution(elements)
    best_solution=current_solution[:]

