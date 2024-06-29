import time
import psutil
import argparse
import pandas as pd
import matplotlib.pyplot as plt
from optimize import generate_neighbors, generate_random_solution
from tabu_algorithm import tabu_search
from hill_climbing_new import hill_climbing_deterministic, hill_climbing_random


def measure_performance(func, *args):
    start_time = time.time()
    process = psutil.Process()
    start_memory = process.memory_info().rss
    result= func(*args)
    end_memory = process.memory_info().rss
    end_time = time.time()
    return {
        "result": result[:2], #best solution and best residue
        "residues": result[2], #convergence data
        "execution_time": end_time - start_time,
        "memory_usage": end_memory - start_memory
    }


def run_experiments(elements, target, iterations, tabu_size):
    results = []
    # Tabu Search
    tabu_result = measure_performance(tabu_search, elements, target, iterations, tabu_size)
    results.append({
        "method": "Tabu Search",
        "residue": tabu_result["result"][1],
        "execution_time": tabu_result["execution_time"],
        "memory_usage": tabu_result["memory_usage"],
        "convergence": tabu_result["residues"]
    })

    # Hill Climbing Deterministic
    hc_det_result = measure_performance(hill_climbing_deterministic, elements, target, iterations)
    results.append({
        "method": "Hill Climbing Deterministic",
        "residue": hc_det_result["result"][1],
        "execution_time": hc_det_result["execution_time"],
        "memory_usage": hc_det_result["memory_usage"],
        "convergence": hc_det_result["residues"]
    })

    # Hill Climbing Random
    hc_rand_result = measure_performance(hill_climbing_random, elements, target, iterations)
    results.append({
        "method": "Hill Climbing Random",
        "residue": hc_rand_result["result"][1],
        "execution_time": hc_rand_result["execution_time"],
        "memory_usage": hc_rand_result["memory_usage"],
        "convergence": hc_rand_result["residues"]
    })

    return results


def plot_results(results):
    df = pd.DataFrame(results)

    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 15))

    # Plot residues
    ax1.bar(df["method"], df["residue"], color='blue')
    ax1.set_title("Residue Comparison")
    ax1.set_ylabel("Residue")

    # Plot execution time
    ax2.bar(df["method"], df["execution_time"], color='green')
    ax2.set_title("Execution Time Comparison")
    ax2.set_ylabel("Time (s)")

    # Plot convergence curves
    for result in results:
        ax3.plot(result["convergence"], label=result["method"])
    ax3.set_title("Convergence Curves")
    ax3.set_xlabel("Iterations")
    ax3.set_ylabel("Residue")
    ax3.legend()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run optimization algorithms and compare their performance")
    parser.add_argument("--input", type=str, required=True, help="Input file containing the set of numbers")
    parser.add_argument("--target", type=int, required=True, help="Target sum")
    parser.add_argument("--iterations", type=int, required=True, help="Number of iterations")
    parser.add_argument("--tabu_size", type=int, required=True, help="Size of the tabu list")

    args = parser.parse_args()

    with open(args.input, 'r') as file:
        elements = list(map(int, file.read().strip().split()))

    target = args.target
    iterations = args.iterations
    tabu_size = args.tabu_size

    results = run_experiments(elements, target, iterations, tabu_size)
    plot_results(results)

    # Output detailed results for each method
    for result in results:
        print(f"Method: {result['method']}")
        print(f"Residue: {result['residue']}")
        print(f"Execution Time: {result['execution_time']}s")
        print(f"Memory Usage: {result['memory_usage']} bytes")
        print("=" * 40)
# TORUN: python src/experiment.py --input data/sample_input.txt --target 10 --iterations 10 --tabu_size 5
