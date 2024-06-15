#algorytm bardzo nieefektywny O(2^n*n), dlatego mały trik sprawdzenia czy target jest mniejszy niż największy element listy
from generate_rand_set import generate_random_set
from optimize import subset_sum_objective, generate_random_solution
import argparse
def powerset(elements):
    s = list(elements)
    result = [[]]

    for elem in s:
        new_subsets =[]
        for subset in result:
            new_subset = subset + [elem]
            new_subsets.append(new_subset)
        result.extend(new_subsets)

    return result

def exhaustive_search(elements, target):
    for subset in powerset(elements):
        if subset_sum_objective(subset, target):
            return subset
    return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Exhaustive search for subset sum problem")
    parser.add_argument("--input", type=str, required=True, help="Input file containing the set of numbers")
    parser.add_argument("--target", type=int, required=True, help="Target sum to find in the subsets")

    args = parser.parse_args()

    with open(args.input, 'r') as file:
        elements = list(map(int, file.read().strip().split()))

    target = args.target

    print("Input Set:", elements)
    print("Target Sum:", target)
    if target>max(elements):
        print("Target sum exceeds maximum number")
    else:
        solution = exhaustive_search(elements, target)
        if solution:
            print(f"Subset found that sums to {target}: {solution}")
        else:
            print(f"No subset found that sums to {target}")
