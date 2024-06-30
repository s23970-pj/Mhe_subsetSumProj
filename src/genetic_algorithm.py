import random
import argparse
from optimize import generate_random_solution
from crossover_method import crossover_one_point, crossover_two_points
from mutation_method import mutation_flip_bit, mutation_swap_bits
from termination_method import termination_min_residue, termination_max_iterations

def residue(solution, elements, target):
    subset_sum = sum([elements[i] for i in range(len(solution)) if solution[i] == 1])
    return abs(subset_sum - target)

def select_parents(population, fitness):
    total_fitness = sum(fitness)
    selection_probs = [f / total_fitness for f in fitness]
    parent1, parent2 = random.choices(population, weights=selection_probs, k=2)
    return parent1, parent2

def genetic_algorithm(elements, target, population_size, max_iterations, crossover_method, mutation_method, termination_method, elitism=False):

    population = [generate_random_solution(len(elements)) for _ in range(population_size)]

    best_solution = min(population, key=lambda sol: residue(sol, elements, target)) #

    best_residue = residue(best_solution, elements, target)

    for iteration in range(max_iterations):
        fitness = [1 / (residue(sol, elements, target) + 1) for sol in population] # określenie

        new_population = []
        if elitism:
            elite = best_solution
            new_population.append(elite)

        while len(new_population) < population_size:
            parent1, parent2 = select_parents(population, fitness)
            child1, child2 = crossover_method(parent1, parent2)
            child1 = mutation_method(child1)
            child2 = mutation_method(child2)
            new_population.extend([child1, child2])

        population = new_population[:population_size]

        current_best_solution = min(population, key=lambda sol: residue(sol, elements, target))
        current_best_residue = residue(current_best_solution, elements, target)

        if current_best_residue < best_residue:
            best_solution = current_best_solution
            best_residue = current_best_residue

        if termination_method(iteration, best_residue):
            break

    return best_solution, best_residue

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ALGORYTM GENETYCZNY DLA SUMY PODZBIORU, GENETIC ALGORITHM FOR SUBSETSUM")
    parser.add_argument("--input", type=str, required=True, help="Input file containing the set of numbers")
    parser.add_argument("--target", type=int, required=True, help="Target sum to find in the subsets")
    parser.add_argument("--population", type=int, required=True, help="Population size")
    parser.add_argument("--iterations", type=int, required=True, help="Maximum number of iterations")
    parser.add_argument("--crossover", type=str, required=True, choices=['one_point', 'two_points'], help="Crossover method")
    parser.add_argument("--mutation", type=str, required=True, choices=['flip_bit', 'swap_bits'], help="Mutation method")
    parser.add_argument("--termination", type=str, required=True, choices=['max_iterations', 'min_residue'], help="Termination method")
    parser.add_argument("--elit", action='store_true', help="Use elitism")

    args = parser.parse_args()

    with open(args.input, 'r') as file:
        content = file.read().strip()
    elements = list(map(int, content.split()))

    if args.crossover == 'one_point':
        crossover_method = crossover_one_point
    elif args.crossover == 'two_points':
        crossover_method = crossover_two_points

    if args.mutation == 'flip_bit':
        mutation_method = mutation_flip_bit
    elif args.mutation == 'swap_bits':
        mutation_method = mutation_swap_bits

    if args.termination == 'max_iterations':
        termination_method = lambda iteration, _: termination_max_iterations(iteration, args.iterations)
    elif args.termination == 'min_residue':
        termination_method = lambda _, residue: termination_min_residue(residue, args.target)

    best_solution, best_residue = genetic_algorithm(elements, args.target, args.population, args.iterations,
                                                    crossover_method, mutation_method, termination_method, args.elit)

    print(f"Best subset found: {[elements[i] for i in range(len(best_solution)) if best_solution[i] == 1]} with residue: {best_residue}")

# RUN:  python src/genetic_algorithm.py --input data/sample_input.txt --target 10 --population 50 --iterations 1000 --crossover one_point --mutation flip_bit --termination max_iterations --elit
# PRZYGOTOWAĆ PARĘ GOTOWYCH POLECEŃ NA POKAZANIE SZYBKO

#Polecenie 1: do przeprowadzenia na małej bazie do 100 elementów, z argumentem --elit i bez
#python src/generate_rand_set.py --size 100 --min_value 1 --max_value 100
#python src/genetic_algorithm.py --input data/sample_input.txt --target 10 --population 50 --iterations 1000 --crossover one_point --mutation flip_bit --termination max_iterations --elit
#python src/genetic_algorithm.py --input data/sample_input.txt --target 10 --population 50 --iterations 1000 --crossover one_point --mutation flip_bit --termination max_iterations

#Polecenia 2: Aby zauważyć rozbieżność między posiadaniem elity i jej brakiem
#python src/generate_rand_set.py --size 300 --min_value 1 --max_value 100
#python src/genetic_algorithm.py --input data/sample_input.txt --target 54 --population 50 --iterations 1000 --crossover one_point --mutation flip_bit --termination max_iterations --elit with residue: 0
#python src/genetic_algorithm.py --input data/sample_input.txt --target 54 --population 50 --iterations 1000 --crossover one_point --mutation flip_bit --termination max_iterations with residue: 2000

#Polecenia 3: (Również dla zestawu 300 elementów)
#python src/genetic_algorithm.py --input data/sample_input.txt --target 90 --population 50 --iterations 1000 --crossover two_points --mutation swap_bits --termination min_residue --elit with residue: 86
#python src/genetic_algorithm.py --input data/sample_input.txt --target 90 --population 50 --iterations 1000 --crossover two_points --mutation swap_bits --termination min_residue with residue: 84
#Author: Adrian Goik s23970