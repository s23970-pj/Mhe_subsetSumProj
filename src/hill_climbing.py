# src/hill_climbing.py

import random
import argparse
from optimize import generate_neighbors

def hill_climbing(elements, target):
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

def random_hill_climbing(elements, target):
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
    parser = argparse.ArgumentParser(description="Hill climbing algorithm for subset sum problem")
    parser.add_argument("--input", type=str, required=True, help="Input file containing the set of numbers")
    parser.add_argument("--target", type=int, required=True, help="Target sum to find in the subsets")

    args = parser.parse_args()

    with open(args.input, 'r') as file:
        elements = list(map(int, file.read().strip().split()))

    target = args.target

    print("Input Set:", elements)
    print("Target Sum:", target)
    if target > sum(elements):
        print("Target sum exceeds the sum of all numbers in the set")
    else:
        solution = hill_climbing(elements, target)
        solution_2 = random_hill_climbing(elements, target)
        if solution and sum(solution) == target:
            print(f"Subset found that sums to {target} using hill climbing: {solution}")
        else:
            print(f"No subset found that sums to {target} using hill climbing")

        if solution_2 and sum(solution_2) == target:
            print(f"Subset found that sums to {target} using random hill climbing: {solution_2}")
        else:
            print(f"No subset found that sums to {target} using random hill climbing")
