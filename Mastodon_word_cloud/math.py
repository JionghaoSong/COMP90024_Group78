import random


def simulate_last_safe_position(n, iterations):
    last_positions = []

    for _ in range(iterations):
        people = list(range(1, n + 1))  # Create a list of people numbered 1 to n
        while len(people) > 1:
            # Generate list of odd indices (considering that Python uses 0-based indexing)
            odd_indices = [i for i in range(len(people)) if i % 2 == 0]
            # Randomly remove one person from an odd index
            if odd_indices:
                remove_index = random.choice(odd_indices)
                del people[remove_index]

        # Append the last remaining person's initial position
        last_positions.append(people[0])

    return last_positions


# Simulate the process for 600 people, 10,000 iterations to get a good distribution
results = simulate_last_safe_position(600, 10000)
print(results[:10])  # Show the first 10 results to check


# [213, 548, 457, 263, 573, 398, 223, 343, 339, 335]