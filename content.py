import random


QUOTES = [
    "Believe in yourself and keep moving forward.",
    "Success comes from consistent effort.",
    "Every expert was once a beginner.",
    "Small steps every day lead to big results.",
    "Never stop learning and improving."
]


JOKES = [
    "Why did the developer go broke? Because they used up all their cache.",
    "Why do programmers prefer dark mode? Because light attracts bugs.",
    "Why was the computer cold? It left its Windows open.",
    "Why did the function return early? It had a short execution span.",
    "What do computers eat for a snack? Microchips."
]


FACTS = [
    "A day on Venus is longer than its year.",
    "Octopuses have three hearts.",
    "Honey can remain edible for a very long time when properly stored.",
    "The human brain contains billions of neurons.",
    "Bananas are botanically classified as berries."
]


def get_random_quote():
    """Return a random motivational quote."""
    return random.choice(QUOTES)


def get_random_joke():
    """Return a random joke."""
    return random.choice(JOKES)


def get_random_fact():
    """Return a random fact."""
    return random.choice(FACTS)
