# src/hill_climbing.py

import random
import argparse
from optimize import generate_neighbors

def hill_climbing_deterministic(elements, target):
    current_set = random.sample(elements, random.randint(1, len(elements)))
    while True:
        current_sum = sum(current_set)
        if current_sum == target:
            return current_set
        neighbors = generate_neighbors(current_set, elements)
        next_set = max(neighbors, key=lambda s: min(sum(s), target) - sum(s))
        if sum(next_set) == current_sum:
            break
        current_set = next_set
    return current_set

def hill_climbing_random(elements, target):
    current_set = random.sample(elements, random.randint(1, len(elements)))
    while True:
        current_sum = sum(current_set)
        if current_sum == target:
            return current_set
        neighbors = generate_neighbors(current_set, elements)
        next_set = random.choice(neighbors)
        if sum(next_set) == current_sum:
            break
        current_set = next_set
    return current_set

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Algorytm wspinaczkowy dla problemu sumy podzbiorów")
    parser.add_argument("--input", type=str, required=True, help="Plik wejściowy zawierający zestaw liczb")
    parser.add_argument("--target", type=int, required=True, help="Docelowa suma do znalezienia w podzbiorach")
    parser.add_argument("--type", type=str, required=True, choices=['deterministic', 'random'], help="Typ algorytmu wspinaczkowego do użycia")

    args = parser.parse_args()

    with open(args.input, 'r') as file:
        elements = list(map(int, file.read().strip().split()))

    target = args.target

    print("Zestaw wejściowy:", elements)
    print("Docelowa suma:", target)

    if args.type == 'deterministic':
        solution = hill_climbing_deterministic(elements, target)
    else:
        solution = hill_climbing_random(elements, target)

    if solution and sum(solution) == target:
        print(f"Podzbiór znaleziony, który sumuje się do {target} używając {args.type} algorytmu wspinaczkowego: {solution}")
    else:
        print(f"Nie znaleziono podzbioru, który sumuje się do {target} używając {args.type} algorytmu wspinaczkowego")
