import random
random_numbers = [random.randint(1, 10) for _ in range(20)]
unique_numbers = set(random_numbers)
print("Original random numbers: ", random_numbers)
print("Original unique numbers: ", unique_numbers)