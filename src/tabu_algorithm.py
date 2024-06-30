from optimize import generate_neighbors, generate_random_solution
import random
import pandas as pd
import argparse

def residue(solution, elements, target):
    subset_sum = sum([elements[i] for i in range(len(solution)) if solution[i] == 1])
    return abs(subset_sum - target)

def tabu_search(elements, target, r, tabu_size):
    list_length = len(elements)  # tutaj przekazanie długości listy elementów
    current_solution = generate_random_solution(list_length)
    best_solution = current_solution
    best_residue = residue(current_solution, elements, target)
    tabu_list = []
    tabu_history = []
    residues = [] #dla eksperymentu

    for iteration in range(r):
        print(f"iteracja {iteration+1}")
        print(f"current solution: {[elements[i] for i in range(len(current_solution)) if current_solution[i] == 1]}")
        print(f"Current Residue: {residue(current_solution, elements, target)}")
        print(f"Best Solution so far: {[elements[i] for i in range(len(best_solution)) if best_solution[i] == 1]}")
        print(f"Best Residue so far: {best_residue}")
        print("=" * 40)
        neighbors = generate_neighbors(current_solution)
        feasible_neighbors = [n for n in neighbors if n not in tabu_list]

        if not feasible_neighbors:  # zaimplementowany mechanizm cofania
            if tabu_history: #sprawdzenie czy lista jest pusta
                current_solution=tabu_history.pop() #wróć nazad
                continue
            else:
                break

        best_neighbor = min(feasible_neighbors, key=lambda s: residue(s, elements, target))
        best_neighbor_residue = residue(best_neighbor, elements, target)
        residues.append(best_residue)

        if best_neighbor_residue < best_residue:
            best_solution = best_neighbor
            best_residue = best_neighbor_residue
        if best_residue == 0:
            break  #warunek zakończenia
        tabu_list.append(current_solution)
        if len(tabu_list) > tabu_size:  # usunięcie najstarszego rozwiązania jeżeli nasza lista długością przekracza rozmiar tabu
            tabu_list.pop(0)
        tabu_history.append(current_solution)
        #print(tabu_history)
        current_solution = best_neighbor

    return best_solution, best_residue, residues

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ALGORYTM TABU")
    parser.add_argument("--input", type=str, required=True, help="Input file containing the set of numbers")
    parser.add_argument("--target", type=int, required=True, help="Target sum to find in the subsets")
    parser.add_argument("--tabu_size", type=int, required=True, help="Size of the Tabu list")
    parser.add_argument("--r", type=int, required=True, help="Number of iterations for the search")

    args = parser.parse_args()

    with open(args.input, 'r') as file:
        elements = list(map(int, file.read().strip().split()))

    best_solution, best_residue, residues = tabu_search(elements, args.target, args.r, args.tabu_size)

    print(
        f"Best subset found: {[elements[i] for i in range(len(best_solution)) if best_solution[i] == 1]} with residue: {best_residue}")

# TORUN: python src/tabu_algorithm.py --input data/sample_input.txt --target 10 --tabu_size 5 --r 100
