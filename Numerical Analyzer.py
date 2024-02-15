import random

def find_rare_even(numbers, rarity_threshold=0.1):
    even_numbers = [num for num in numbers if num % 2 == 0]
    if not even_numbers:
        return None

    rare_even_indices = [i for i, num in enumerate(even_numbers) if num / sum(even_numbers) < rarity_threshold]
    if not rare_even_indices:
        return None

    return even_numbers[random.choice(rare_even_indices)]

def simulate_rare_even_occurrences(problem_function, problem_args, trials=1000):
    rare_even_counts = 0
    results = []
    for _ in range(trials):
        output = problem_function(*problem_args)
        rare_even_number = find_rare_even(output)
        if rare_even_number:
            rare_even_counts += 1
            results.append(rare_even_number)

if __name__ == "__main__":
    # Example 1: Finding a rare even sum in a random list
    numbers = [random.randint(-10, 10) for _ in range(10)]
    print(find_rare_even(numbers))

    # Example 2: Simulating rare even outcomes in a specific problem
    # Replace with your actual problem function and arguments
    def my_problem_function(arg1, arg2):
        # ... perform your problem calculations here
        return some_output_data

    rare_even_counts, statistics = simulate_rare_even_occurrences(
        my_problem_function, args=(1, 2), trials=5000
    )
    print(f"Rare even counts: {rare_even_counts}")
    print(f"Statistics: {statistics}")
