#!/usr/bin/python3
"""Say hello to the world"""

import random

# List of greeting messages
greetings = [
    "Hello!",
    "Hi there!",
    "Greetings!",
    "Howdy!",
    "Welcome!",
    "Good day!",
    "Hey!"
]

# Randomly choose a greeting
random_greeting = random.choice(greetings)

# Print the selected greeting
print(random_greeting[::-1])
