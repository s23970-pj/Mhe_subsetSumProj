import random
import argparse

def generate_random_set(size, min_value, max_value):
    return [random.randint(min_value, max_value) for _ in range(size)]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a random set of numbers and save to a file")
    parser.add_argument("--size", type=int, required=True, help="Size of the random set")
    parser.add_argument("--min_value", type=int, required=True, help="Minimum value for the random numbers")
    parser.add_argument("--max_value", type=int, required=True, help="Maximum value for the random numbers")

    args = parser.parse_args()

    random_set = generate_random_set(args.size, args.min_value, args.max_value)

    print("Generated Set:", random_set)

    # Save to file - separated by space, 'w' argument nadpisanie danych
    with open('data/sample_input.txt', 'w') as file:
        file.write(' '.join(map(str, random_set)))
