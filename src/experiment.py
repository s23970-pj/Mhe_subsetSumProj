import random
import pandas as pd
import time
import argparse
from hill_climbing_new import hill_climbing_deterministic, hill_climbing_random
from tabu_algorithm import tabu_search
from genetic_algorithm import genetic_algorithm

def run_experiments(elements, target, hill_climbing_params, tabu_search_params, ga_params): #sa params
    results = []

    # Hill Climbing Deterministic
    for r in hill_climbing_params['iterations']:
        start_time = time.time()
        best_solution, best_residue = hill_climbing_deterministic(elements, target, r)
        duration = time.time() - start_time
        results.append(('Hill Climbing Deterministic', r, None, best_residue, duration))

    # Hill Climbing Random
    for r in hill_climbing_params['iterations']:
        start_time = time.time()
        best_solution, best_residue = hill_climbing_random(elements, target, r)
        duration = time.time() - start_time
        results.append(('Hill Climbing Random', r, None, best_residue, duration))

    # Tabu Search
    for r, tabu_size in tabu_search_params:
        start_time = time.time()
        best_solution, best_residue = tabu_search(elements, target, r, tabu_size)
        duration = time.time() - start_time
        results.append(('Tabu Search', r, tabu_size, best_residue, duration))
    #
    # # Simulated Annealing
    # for temp, cooling_rate, max_iter in sa_params:
    #     start_time = time.time()
    #     best_solution, best_residue = simulated_annealing(elements, target, temp, cooling_rate, max_iter)
    #     duration = time.time() - start_time
    #     results.append(('Simulated Annealing', max_iter, None, best_residue, duration))

    # Genetic Algorithm
    for pop_size, max_iter, crossover, mutation, elitism in ga_params:
        start_time = time.time()
        best_solution, best_residue = genetic_algorithm(elements, target, pop_size, max_iter, crossover, mutation, elitism)
        duration = time.time() - start_time
        results.append(('Genetic Algorithm', max_iter, None, best_residue, duration))

    return pd.DataFrame(results, columns=['Method', 'Iterations', 'Tabu Size', 'Best Residue', 'Duration'])

if __name__ == "__main__":
    elements = [random.randint(1, 100) for _ in range(50)]
    target = 500

    hill_climbing_params = {
        'iterations': [100, 200, 300, 400, 500]
    }

    tabu_search_params = [
        (100, 5), (200, 5), (300, 5), (400, 5), (500, 5),
        (100, 10), (200, 10), (300, 10), (400, 10), (500, 10)
    ]

    # sa_params = [
    #     (1000, 0.95, 1000), (1000, 0.95, 2000), (1000, 0.95, 3000)
    # ]

    ga_params = [
        (50, 1000, 'one_point', 'flip_bit', True),
        (50, 2000, 'two_points', 'swap_bits', True),
        (50, 3000, 'one_point', 'flip_bit', False)
    ]

    results = run_experiments(elements, target, hill_climbing_params, tabu_search_params, ga_params) #sa params

    # Zapis wyników do pliku CSV
    results.to_csv('data/experiment_results.csv', index=False)

    # Analiza wyników
    print(results)
