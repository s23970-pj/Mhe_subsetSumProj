def hill_climbing(numbers, target):
    current_set = generate_random_set(numbers)
    while True:
        current_sum = sum(current_set)
        if current_sum == target:
            return current_set
        neighbors = generate_neighbors(current_set, numbers)
        next_set = max(neighbors, key=lambda s: min(sum(s), target) - sum(s))
        if sum(next_set) == current_sum:
            break
        current_set = next_set
    return None
def random_hill_climbing(numbers, target):
    current_set = generate_random_set(numbers)
    while True:
        current_sum = sum(current_set)
        if current_sum == target:
            return current_set
        neighbors = generate_neighbors(current_set, numbers)
        next_set = random.choice(neighbors)
        if sum(next_set) == current_sum:
            break
        current_set = next_set
    return None
