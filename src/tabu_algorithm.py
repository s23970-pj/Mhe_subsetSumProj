from optimize import generate_random_solution, generate_neighbors, subset_sum_objective
import argparse


def tabu_search(elements, target, r):
    current_solution=generate_random_solution(elements)
    best_solution=current_solution[:]
    best_residue = subset_sum_objective(best_solution, target)

#
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ALGORYTM TABU")
    parser.add_argument("--input", type=str, required=True, help="Input file containing the set of numbers")
    parser.add_argument("--target", type=int, required=True, help="Target sum to find in the subsets")
    parser.add_argument("--tabu_size", type=int, required=True, help="Size of the Tabu list")
    parser.add_argument("--r", type=int, required=True, help="Number of iterations for the search")

    args = parser.parse_args()

    with open(args.input, 'r') as file:
        elements = list(map(int, file.read().strip().split()))

    print("Generated Set:", elements)

    solution, residue = tabu_search(elements, args.target, args.tabu_size, args.r)

    print("Best Subset Found:", solution)
    print("Best Residue:", residue)

