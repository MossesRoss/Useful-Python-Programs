#Program by Mosses Ross
import random

def probability_experiment(num_trials, event_condition):
    event_occurrences = 0

    for _ in range(num_trials):
        if event_condition():
            event_occurrences += 1

    probability = event_occurrences / num_trials
    return probability

def dice_roll():
    return random.randint(1, 6)

num_trials = 10000
probability_of_six = probability_experiment(num_trials, lambda: dice_roll() == 6)
print(f"The probability of rolling a six is approximately: {probability_of_six}")
