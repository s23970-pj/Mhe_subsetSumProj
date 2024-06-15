import random
import argparse
from optimize import generate_neighbors

def residue(subset, target):
    return abs(sum(subset) - target)

def hill_climbing_deterministic(elements, target, r):
    current_subset = random.sample(elements, random.randint(1, len(elements)))
    for _ in range(r):
        neighbors = generate_neighbors(current_subset, elements)
        next_set = min(neighbors, key=lambda s: residue(s, target))
        if residue(next_set, target) >= residue(current_subset, target):
            break
        current_subset = next_set
    return current_subset, residue(current_subset, target)

def hill_climbing_random(elements, target, r):
    current_subset = random.sample(elements, random.randint(1, len(elements)))
    for _ in range(r):
        neighbors = generate_neighbors(current_subset, elements)
        next_set = random.choice(neighbors)
        if residue(next_set, target) >= residue(current_subset, target):
            break
        current_subset = next_set
    return current_subset, residue(current_subset, target)

def hill_climbing(elements, target, q, r): #max ilosc prób, r tutaj muszę ograniczyć iteracje (poprzedni problem z whilem)
    best_residue_deterministic = float('inf')
    best_subset_deterministic = None

    best_residue_random = float('inf')
    best_subset_random = None

    for _ in range(q):
        subset_deterministic, res_deterministic = hill_climbing_deterministic(elements, target, r)
        subset_random, res_random = hill_climbing_random(elements, target, r)

        if res_deterministic < best_residue_deterministic:
            best_residue_deterministic = res_deterministic
            best_subset_deterministic = subset_deterministic

        if res_random < best_residue_random:
            best_residue_random = res_random
            best_subset_random = subset_random

    return (best_subset_deterministic, best_residue_deterministic), (best_subset_random, best_residue_random)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="OPIS PL: Algorytm Wspinaczkowy: Program uruchamia algorytm wspinaczkowy w dwóch rodzajach podejść do problemu\n"
                                                 "użyj polecenia $ python src/hill_climbing.py --input data/sample_input.txt --target [x] --q [ilość random subset] --r [liczba iteracji]" )
    parser.add_argument("--input", type=str, required=True, help="Input file containing the set of numbers")
    parser.add_argument("--target", type=int, required=True, help="Target sum to find in the subsets")
    parser.add_argument("--q", type=int, required=True, help="Number of times to choose a random subset")
    parser.add_argument("--r", type=int, required=True, help="Number of hill climbing iterations per subset")

    args = parser.parse_args()

    with open(args.input, 'r') as file:
        elements = list(map(int, file.read().strip().split()))

    target = args.target
    q = args.q
    r = args.r

    print("Input Set:", elements)
    print("Target Sum:", target)
    print("Number of random subsets (q):", q)
    print("Number of hill climbing iterations (r):", r)

    (best_subset_deterministic, best_residue_deterministic), (best_subset_random, best_residue_random) = hill_climbing(elements, target, q, r)

    print(f"Deterministic: Best subset found that sums to near {target} with residue {best_residue_deterministic}: {best_subset_deterministic}")
    print(f"Random: Best subset found that sums to near {target} with residue {best_residue_random}: {best_subset_random}")
