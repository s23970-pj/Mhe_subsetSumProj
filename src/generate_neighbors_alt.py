def generate_neighbors(current_solution):
    neighbors = []
    for i in range(len(current_solution)):
        # Flip one bit
        neighbor = current_solution[:]
        neighbor[i] = 1 - neighbor[i]
        neighbors.append(neighbor)

        # Optionally, flip two bits for additional neighbors
        for j in range(i + 1, len(current_solution)):
            neighbor2 = neighbor[:]
            neighbor2[j] = 1 - neighbor2[j]
            neighbors.append(neighbor2)

    return neighbors

# New fucnction for neighbor search. Last one was very time sonsuming as it had to phisically iterate through whole list
#