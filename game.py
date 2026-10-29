import random


def play_guessing_game():
    

    secret_number = random.randint(1, 20)
    attempts = 5

    print(
        "Assistant: I'm thinking of a number between 1 and 20. "
        f"You have {attempts} tries."
    )

    for attempt in range(1, attempts + 1):
        try:
            guess = int(input("Assistant: Guess a number: "))

            if guess < 1 or guess > 20:
                print("Assistant: Enter a number between 1 and 20.")
                continue

        except ValueError:
            print("Assistant: Please enter a valid whole number.")
            continue

        if guess == secret_number:
            print(
                f"Assistant: Correct, {secret_number}! "
                f"You won in {attempt} attempt(s)."
            )
            return

        elif guess < secret_number:
            print("Assistant: Higher!")

        else:
            print("Assistant: Lower!")

    print(
        f"Assistant: Game over! The number was {secret_number}."
    )
