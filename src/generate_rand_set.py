import random

def generate_random_set(size, min_value, max_value):
    return [random.randint(min_value, max_value) for _ in range(size)]

if __name__ == "__main__":
    size = 10 # na razie size 10 potem na potrzeby programów można zwiększyć
    min_value = 1
    max_value = 100
    random_set = generate_random_set(size, min_value, max_value)
    print("Generated Set:", random_set)
