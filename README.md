# Subset Sum Problem Project
## Author : Adrian Goik s23970
## Description

The subset sum problem (SSP) is a decision problem in computer science. In its most general formulation, there is a multiset S
of integers and a target-sum T, and the question is to decide whether any subset of the integers sum to precisely T.
This project explores various optimization algorithms to solve this NP-complete problem.

## Algorithms Implemented

-exhaustive_search<br>
-hill_climbing algorithm with deterministic method and random neighbor selection<br>
-simulated_annealing<br>
-tabu search - with implemented option of reversing on list of solution<br>
-genetic_ algorithm - two crossover methods, two termination methods, two mutation methods<br>
<i>Additionally implemented experiment.py comparing hill climbing algorithm with tabu search. Using convergence curve based on residue.</i>

## Running the Project
<h6>To run this project you have to use terminal command line</h6><br>
Sets of ready to use commands:

1. To gerenerate new random set:
``` 
 python src/generate_rand_set.py --size 20 --min_value 10 --max_value 40  

```
2. Exhaustive search
```
python src/exhaustive_search.py --input data/sample_input.txt --target 10

```
3.hill_climbing
```
python src/hill_climbing_new.py --input data/sample_input.txt --target 10 --q 10 --r 100
```

4.tabu search
```
python src/tabu_algorithm.py --input data/sample_input.txt --target 10 --tabu_size 5 --r 100
```
5.Simulated annealing
```angular2html
#TORUN: python src/simulated_annealing.py --input data/sample_input.txt --target 64 --iterations 1000 --temp_init 100 --cooling_rate 0.3

```
6.Genetic algorithm
```angular2html
# RUN:  python src/genetic_algorithm.py --input data/sample_input.txt --target 10 --population 50 --iterations 1000 --crossover one_point --mutation flip_bit --termination max_iterations --elit

#Polecenie 1: do przeprowadzenia na małej bazie do 100 elementów, z argumentem --elit i bez
#python src/generate_rand_set.py --size 100 --min_value 1 --max_value 100
#python src/genetic_algorithm.py --input data/sample_input.txt --target 10 --population 50 --iterations 1000 --crossover one_point --mutation flip_bit --termination max_iterations --elit
#python src/genetic_algorithm.py --input data/sample_input.txt --target 10 --population 50 --iterations 1000 --crossover one_point --mutation flip_bit --termination max_iterations

#Polecenia 2: Aby zauważyć rozbieżność między posiadaniem elity i jej brakiem
#python src/generate_rand_set.py --size 300 --min_value 1 --max_value 100
#python src/genetic_algorithm.py --input data/sample_input.txt --target 54 --population 50 --iterations 1000 --crossover one_point --mutation flip_bit --termination max_iterations --elit with residue: 0
#python src/genetic_algorithm.py --input data/sample_input.txt --target 54 --population 50 --iterations 1000 --crossover one_point --mutation flip_bit --termination max_iterations with residue: 2000

#Polecenia 3: (Również dla zestawu 300 elementów)
#python src/genetic_algorithm.py --input data/sample_input.txt --target 90 --population 50 --iterations 1000 --crossover two_points --mutation swap_bits --termination min_residue --elit with residue: 86
#python src/genetic_algorithm.py --input data/sample_input.txt --target 90 --population 50 --iterations 1000 --crossover two_points --mutation swap_bits --termination min_residue with residue: 84

```
### Requirements

- [Programming Language] (e.g., Python 3.11)
- [Required Libraries] (random, argparse, matplotlib, pandas,psutil, time, sklearn)

### Usage

Run any of the algorithms from the command line:

```bash
TO GENERATE NEW SETS OF DATA:
python src/generate_rand_set.py --size [size of multiset] --min_value [value] --max_value [value]  //to be completed with precise information

TO RUN DESIRED ALGORITHM:
python ./src/exhaustive_search.py --input data\sample_input.txt --target 100



