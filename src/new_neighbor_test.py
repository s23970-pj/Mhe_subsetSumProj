import random
def generate_neighbors(current_solution):
    neighbors = []
    for i in range(len(current_solution)):
        # Flip one bit
        neighbor = current_solution[:]
        neighbor[i] = 1 - neighbor[i]
        neighbors.append(neighbor)
        print("a",neighbor)

        # Optionally, flip two bits for additional neighbors
        for j in range(i + 1, len(current_solution)):
            neighbor2 = neighbor[:]
            neighbor2[j] = 1 - neighbor2[j]
            neighbors.append(neighbor2)
            print("b",neighbor2)

    return neighbors

# New fucnction for neighbor search. Last one was very time sonsuming as it had to phisically iterate through whole list
#\
def generate_random_solution(length):
    return [random.randint(0, 1) for _ in range(length)]
if __name__ == '__main__':
    rand_solution = generate_random_solution(8)
    print("list", rand_solution)
    generate_neighbors(rand_solution)
