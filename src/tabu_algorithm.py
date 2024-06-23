from optimize import generate_random_solution, subset_sum_objective
from generate_neighbors_alt import generate_neighbors
import argparse
import random
import time


def residue(solution, elements, target):
    subset_sum = sum([elements[i] for i in range(len(solution)) if solution[i] == 1])
    return abs(subset_sum - target)


def initialize_solution(n):
    return [random.randint(0, 1) for _ in range(n)]


def tabu_search(elements, target, max_iterations, tabu_tenure, time_limit):
    start_time = time.time()
    n = len(elements)
    current_solution = initialize_solution(n)
    best_solution = current_solution
    tabu_list = []
    tabu_dict = {}
    backtrack_point = None

    for _ in range(max_iterations):
        if time.time() - start_time > time_limit:
            break

        neighbors = generate_neighbors(current_solution)
        feasible_neighbors = [n for n in neighbors if tuple(n) not in tabu_dict]

        if not feasible_neighbors:
            if backtrack_point:
                current_solution = backtrack_point
                continue
            else:
                break

        best_neighbor = min(feasible_neighbors, key=lambda s: residue(s, elements, target))

        if residue(best_neighbor, elements, target) < residue(best_solution, elements, target):
            best_solution = best_neighbor
            backtrack_point = best_neighbor  # Update backtrack point

        tabu_list.append(current_solution)
        tabu_dict[tuple(current_solution)] = tabu_tenure

        current_solution = best_neighbor

        # Update tabu list and decrease tenure
        for solution in list(tabu_dict.keys()):
            tabu_dict[solution] -= 1
            if tabu_dict[solution] <= 0:
                del tabu_dict[solution]

    return best_solution, residue(best_solution, elements, target)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ALGORYTM TABU")
    parser.add_argument("--input", type=str, required=True, help="Input file containing the set of numbers")
    parser.add_argument("--target", type=int, required=True, help="Target sum to find in the subsets")
    parser.add_argument("--tabu_size", type=int, required=True, help="Size of the Tabu list")
    parser.add_argument("--r", type=int, required=True, help="Number of iterations for the search")
    parser.add_argument("--time_limit", type=int, required=False, default=10, help="Time limit for the search in seconds")

    args = parser.parse_args()

    with open(args.input, 'r') as file:
        elements = list(map(int, file.read().strip().split()))

    print("Generated Set:", elements)

    best_solution, best_residue = tabu_search(elements, args.target, args.r, args.tabu_size, args.time_limit)

    print(f"Best subset found: {[elements[i] for i in range(len(best_solution)) if best_solution[i] == 1]} with residue: {best_residue}")

# TORUN: python src/tabu_algorithm.py --input data/sample_input.txt --target 10 --tabu_size 5 --r 100 --time_limit 10