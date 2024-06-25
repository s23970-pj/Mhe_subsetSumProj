from optimize import generate_neighbors,generate_random_solution
import random
def residue(solution, elements, target):
    subset_sum = sum([elements[i] for i in range(len(solution)) if solution[i] == 1])
    return abs(subset_sum - target)


def update_temperature(initial_temp, cooling_rate, iteration):

    cooling_factor = cooling_rate ** iteration # współczynnik schładzania ppo potęgi iterancji

    # nowa temperatura
    new_temp = initial_temp * cooling_factor

    return new_temp

def decide_accept(current_residue, next_residue, current_temp):
    delta_r = next_residue - current_residue
    if delta_r < 0:
        return True
    else:
        return random.uniform(0, 1) < math.exp(-delta_r / current_temp)


def simulated_annealing(elements, target, iterations, initial_temp, cooling_rate): #all given by user
    current_solution = generate_random_solution(len(elements))
    best_solution = current_solution
    current_temp = initial_temp

    for iteration in range(iterations):
        current_residue = residue(current_solution, elements, target)
        best_residue = residue(best_solution, elements, target)

        if current_residue < best_residue:
            best_solution = current_solution

        neighbors = generate_neighbors(current_solution)

        # Choose a neighbor using a normal distribution
        # HOW TO CHOOSE
        #

        if decide_accept(current_residue, next_residue, current_temp):
            current_solution = next_solution

        current_temp = update_temperature(initial_temp, cooling_rate, iteration)

        if current_temp <= 0:
            break

    return best_solution, residue(best_solution, elements, target)











# SKOPIOWANE Z TABU DOSTOSUJE JAK NAPISZE RESZTE
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Algorytm symulowanego wyżarzania ")
    parser.add_argument("--input", type=str, required=True, help="Input file containing the set of numbers")
    parser.add_argument("--target", type=int, required=True, help="Target sum to find in the subsets")
    parser.add_argument("--tabu_size", type=int, required=True, help="Size of the Tabu list")
    parser.add_argument("--r", type=int, required=True, help="Number of iterations for the search")

    args = parser.parse_args()

    with open(args.input, 'r') as file:
        elements = list(map(int, file.read().strip().split()))

    best_solution, best_residue = tabu_search(elements, args.target, args.r, args.tabu_size)

    print(
        f"Best subset found: {[elements[i] for i in range(len(best_solution)) if best_solution[i] == 1]} with residue: {best_residue}")
