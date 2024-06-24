














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
